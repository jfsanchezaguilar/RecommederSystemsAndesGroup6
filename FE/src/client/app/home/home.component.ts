import { Component, OnInit } from '@angular/core';
import { RecommendTask, TaskStatus } from "../models/RecommendTask";
import { RecommendTaskService } from "../services/recommendtasks.service";
import * as moment from 'moment';
import { BookUser, Book, BookRaiting } from "../models/Book";
import { BookService } from "../services/book.service";
import { BookUserService } from "../services/bookusers.service";
import { BookRaitingService } from "../services/bookraitings.service";
/**
 * This class represents the lazy loaded HomeComponent.
 */
@Component({
  moduleId: module.id,
  selector: 'sd-home',
  templateUrl: 'home.component.html',
  styleUrls: ['home.component.css'],
})
export class HomeComponent implements OnInit {

  public trainingSelected: string = "50 - 50";
  public similaritySelected: string = "User-User";
  public algorithms: string[] = ["Jaccard", "Cosine", "Pearson"];
  public algorithmSelected: string = "Jaccard";
  public saveSuccess: boolean = false;
  public recommendTasks: RecommendTask[] = [];
  public recommendTaskSelected: RecommendTask = new RecommendTask();
  public newUserObj: BookUser = new BookUser();
  public newBookObj: Book = new Book();
  public newBookRaitingObj: BookRaiting = new BookRaiting();
  public recommendTasksResult: any[] = [];
  public recommendTasksResultFiltered: any[] = [];
  public isResultNotAvailabel: boolean = false;
  public filterBy: string = "User";
  public filterByTerm: string = "";

  ngOnInit(): void {
    this.updateRecommendTasks();
  }

  constructor(private recommendTaskService: RecommendTaskService, private bookService: BookService, private bookUserService: BookUserService, private bookRaitingService: BookRaitingService) {

  }

  private updateRecommendTasks() {
    this.recommendTaskService.getAll().subscribe((response) => {
      console.log(response);
      this.recommendTasks = response
      if (this.recommendTasks.length > 0) {
        this.recommendTaskSelected = this.recommendTasks[0];
        this.updateRecommendTaskResult();
      }
    });
  }

  private updateRecommendTaskResult() {
    this.isResultNotAvailabel = false;
    this.recommendTaskService.get(this.recommendTaskSelected.id).subscribe((response) => {
      this.recommendTasksResult = JSON.parse(response);
      this.recommendTasksResultFiltered = this.recommendTasksResult;
      if (response == "") {
        this.isResultNotAvailabel = true;
      }
    }, (error: any) => {
      this.isResultNotAvailabel = true;
    });
  }

  onAlgorithmSelected(value: string) {
    this.algorithmSelected = value;
  }

  onSimlaritySelected(value: string) {
    this.similaritySelected = value;
  }

  onTrainingSelected(value: string) {
    this.trainingSelected = value;
  }

  onRecommendTaskSelected(value: RecommendTask) {
    this.recommendTaskSelected = value;
    this.updateRecommendTaskResult();
  }

  onFilterSelected(value: string) {
    this.filterBy = value;
  }

  filterItems() {
    if (this.filterByTerm != "") {
      if (this.filterBy == "User")
        this.recommendTasksResultFiltered = this.recommendTasksResult.filter(result => result.UserID.toString() == this.filterByTerm);
      else if (this.filterBy == "Book")
        this.recommendTasksResultFiltered = this.recommendTasksResult.filter(result => result.ISBN.toString() == this.filterByTerm);
    }else{
      this.recommendTasksResultFiltered = this.recommendTasksResult;
    }
  }

  newRecommendTask() {
    let task: RecommendTask = new RecommendTask();
    task.training = this.getTraining(this.trainingSelected);
    task.similarity = this.getSimilarity(this.similaritySelected);
    task.algorithm = this.algorithmSelected;
    task.status = TaskStatus.added;
    task.added_date = moment().toDate();
    this.recommendTaskService.save(task).subscribe(() => {
      this.saveSuccess = true;
      this.updateRecommendTasks();
      setTimeout(() => {
        this.saveSuccess = false;
      }, 2000);
    });
  }

  newBook() {
    this.bookService.save(this.newBookObj).subscribe(() => {
      this.saveSuccess = true;
      this.newBookObj = new Book();
      setTimeout(() => {
        this.saveSuccess = false;
      }, 2000);
    });
  }

  newUser() {
    this.bookUserService.save(this.newUserObj).subscribe(() => {
      this.saveSuccess = true;
      this.newUserObj = new BookUser();
      setTimeout(() => {
        this.saveSuccess = false;
      }, 2000);
    });
  }

  newBookRaiting() {
    this.bookRaitingService.save(this.newBookRaitingObj).subscribe(() => {
      this.saveSuccess = true;
      this.newBookRaitingObj = new BookRaiting();
      setTimeout(() => {
        this.saveSuccess = false;
      }, 2000);
    });
  }

  private getTraining(trainingSelected: string): number {
    let training: number = 80;
    switch (trainingSelected) {
      case "50 - 50":
        training = 50;
        break;
      case "60 - 40":
        training = 60;
        break;
      case "70 - 30":
        training = 70;
        break;
      case "80 - 20":
        training = 80;
        break;
    }
    return training;
  }

  private getSimilarity(similaritySelected: string): string {
    let similarity: string = "User";
    switch (similaritySelected) {
      case "User-User":
        similarity = "User";
        break;
      case "Item-Item":
        similarity = "Item";
        break;
    }
    return similarity;
  }

}
