import { Injectable } from '@angular/core';
import { Http, Response, URLSearchParams, Headers } from '@angular/http';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import { Observable } from 'rxjs/Rx';
import { RecommendTask } from "../models/RecommendTask";

@Injectable()
export class RecommendTaskService {

    private url: string = 'http://localhost:8000/tasks/';
    private headers: Headers;

    constructor(private http: Http) {
        this.headers = new Headers();
        this.headers.append("Authorization", "Basic " + btoa("root:root1234"));
    }

    save(recommendTask: RecommendTask) {
        this.headers.append("Content-Type", "application/json");
        let json: string = JSON.stringify(recommendTask);
        console.log(json);
        return this.http.post(this.url, JSON.stringify(recommendTask), { headers: this.headers }).map(this.extractData).catch(this.handleError);
    }

    getAll(): Observable<any> {
        return this.http.get(this.url, { headers: this.headers }).map(this.extractData);
    }

    private handleError(error: any) {
        let errMsg = (error.message) ? error.message :
            error.status ? `${error.status} - ${error.statusText}` : 'Server error';
        console.error(errMsg);
        return Observable.throw(errMsg);
    }

    private extractData(res: Response) {
        let body: any;

        // check if empty, before call json
        if (res.text()) {
            body = res.json();
        }

        return body || {};
    }
}