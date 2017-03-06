import { Component } from '@angular/core';

@Component({
  selector: 'home',
  styleUrls: ['./home.component.scss'],
  templateUrl: './home.component.html'
})
export class HomeComponent {
    public trainingSelected: string = "50 - 50";
    public similaritySelected: string = "User-User";
    public algorithms: string[] = ["Jaccard", "Cosine", "Pearson"];
    public algorithmSelected: string = "Jaccard";

    onAlgorithmSelected(value: string) {
        this.algorithmSelected = value;
    }

    onSimlaritySelected(value: string) {
        this.similaritySelected = value;
    }

    onTrainingSelected(value: string) {
        this.trainingSelected = value;
    }
}
