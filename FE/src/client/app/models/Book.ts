export class Book{
    public isbn: string;
    public book_title: string;
    public book_author: string;
    public year_publish: string;
    public publisher: string;
    public image_small: string;
    public image_medium: string;
    public image_large: string;
}

export class BookUser{
    public id: number;
    public user_id: number;
    public location: string;
    public age: number;
}

export class BookRaiting{
    public id: number;
    public user_id: number;
    public isbn: string;
    public raiting: number;
}