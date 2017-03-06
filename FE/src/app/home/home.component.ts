import { Component, ChangeDetectionStrategy  } from '@angular/core';
import { RecommendTask, TaskStatus } from "../shared/classes";
import * as moment from 'moment';
import { RecommendTaskService } from "../services/recommendtasks.service";

@Component({
  selector: 'home',
  styleUrls: ['./home.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './home.component.html',
})
export class HomeComponent {
  public trainingSelected: string = "50 - 50";
  public similaritySelected: string = "User-User";
  public algorithms: string[] = ["Jaccard", "Cosine", "Pearson"];
  public algorithmSelected: string = "Jaccard";
  public saveSuccess: boolean = false;
  public tabs: any[] = [
    { title: 'Dynamic Title 1', content: 'Dynamic content 1' },
    { title: 'Dynamic Title 2', content: 'Dynamic content 2', disabled: true },
    { title: 'Dynamic Title 3', content: 'Dynamic content 3', removable: true }
  ];
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

  newRecommendTask(event) {
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

  setActiveTab(index: number): void {
    this.tabs[index].active = true;
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
