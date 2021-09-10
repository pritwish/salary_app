# Book Logger

An application to log book notes

> This project was built as a part ot [PythonToProject Bootcamp by TheLearningDev](https://bhavaniravi.gumroad.com/l/LaFSj)

## Feature list


## Architecture/Flow Diagram



## API Design

List all the APIs it's methods, request and response params

> Add the API table here

| Action         | Table  | REST Method | Endpoint | Response | Error |
| ---------------| ------ | ----------- | -------- | -------- | ----- |
| add book       | Book   | POST   | /books | 200 | 400 |
| add author     | Author | POST   | /authors | 200 | 400 |
| sign up        | User   | POST   | /users | 200 | 400 |
| Login          | User   | POST   | /users | 200 | 400 |
| add notes      | Notes  | POST   | /book/id/notes | 200 | 400 |
| get all books  | Book   | GET   | /books | 200 | 400 |
| get all authors| Author | GET   | /authors | 200 | 400 |
| get all notes  | Notes  | GET   | /book/id/notes | 200 | 400 |
| get book       | Book   | GET   | /book/id | 200 | 400 |
| get author     | Author | GET   | /author/id | 200 | 400 |
| get notes by id| Notes  | GET   | /book/id/notes/id | 200 | 400 |
| update book    | Book   | PUT   | /book/id | 200 | 400 |
| update author  | Author | PUT   | /author/id | 200 | 400 |
| update notes   | Notes  | PUT   | /book/id/notes/id | 200 | 400 |
| delete book    | Book   | DELETE | /book/id | 200 | 400 |
| delete author  | Author | DELETE | /author/id | 200 | 400 |
| delete notes   | Notes  | DELETE | /book/id/notes/id | 200 | 400 |


## DB Design Diagram

> Add the DB design table here

Table 1 : Book
- id : int (Primary Key)
- book_name : string 
- author : Relationship(M2M)
- published_date : Date
- Category : list of strings
- Price : float
- publisher : Relationship(1:1)

Table 2 :Author
- author_id : int (Primary Key)
- author_name : string
- author_bio : string
- date_of_birth : Date
- experience : int
- Field of work : string

Table 3 : Notes
- id : int (Primary Key)
- book : Book (ForeignKey) 1 book can have multiple notes
- user : Book (ForeigenKey) 1 user can have take multiple notes, for multiple books


## Coding Issues and Learning


## Deployment Instructions



## Repo Setup











