export class RecommendTask{
    public id: number;
    public training: number;
    public similarity: string;
    public algorithm: string;
    public added_date: Date;
    public start_date: Date;
    public finish_date: Date;
    public status: number;
}

export enum TaskStatus {
    added = 0,
    started = 1,
    finished = 2
}