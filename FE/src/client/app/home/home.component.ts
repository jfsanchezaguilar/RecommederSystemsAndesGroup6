import { Component, OnInit } from '@angular/core';
import { RecommendTask, TaskStatus } from "../models/RecommendTask";
import { RecommendTaskService } from "../services/recommendtasks.service";
import * as moment from 'moment';
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

  ngOnInit(): void {
    this.recommendTaskService.getAll().subscribe(response => this.recommendTasks = response.results);
    if (this.recommendTasks.length > 0)
      this.recommendTaskSelected = this.recommendTasks[0];
  }

  constructor(private recommendTaskService: RecommendTaskService) {

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

  onRecommendTaskSelected(value: RecommendTask){
    this.recommendTaskSelected = value;
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
      setTimeout(() => {
        this.saveSuccess = false;
      }, 2000);
    });
  }
  
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
