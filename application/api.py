from application.app import app, db
from flask import request

# Import your models here
from application.models import User, Book, Author, Notes, Category

@app.route("/")
def home():
    return {"Status": "Success"}, 200 

# Write your API endpoints here


# | Action         | Table  | REST Method | Endpoint | Response | Error |
# | ---------------| ------ | ----------- | -------- | -------- | ----- |
# | add book       | Book   | POST   | /books | 200 | 400 |
# | add author     | Author | POST   | /authors | 200 | 400 |
# | sign up        | User   | POST   | /users | 200 | 400 |
# | Login          | User   | POST   | /users | 200 | 400 |
# | add notes      | Notes  | POST   | /book/id/notes | 200 | 400 |
# | get all books  | Book   | GET   | /books | 200 | 400 |
# | get all authors| Author | GET   | /authors | 200 | 400 |
# | get all notes  | Notes  | GET   | /book/id/notes | 200 | 400 |
# | get book       | Book   | GET   | /book/id | 200 | 400 |
# | get author     | Author | GET   | /author/id | 200 | 400 |
# | get notes by id| Notes  | GET   | /book/id/notes/id | 200 | 400 |
# | update book    | Book   | PUT   | /book/id | 200 | 400 |
# | update author  | Author | PUT   | /author/id | 200 | 400 |
# | update notes   | Notes  | PUT   | /book/id/notes/id | 200 | 400 |
# | delete book    | Book   | DELETE | /book/id | 200 | 400 |
# | delete author  | Author | DELETE | /author/id | 200 | 400 |
# | delete notes   | Notes  | DELETE | /book/id/notes/id | 200 | 400 |


@app.route("/book", methods=["POST"])
def add_book():
    # name, author, pages
    params = request.json
    book = Book(name=params["book_name"])
    db.session.add(book)
    db.session.commit()
    return {"id": book.id, "name": book.name, "published_date": book.published_date, "author": book.author}

@app.route("/book/<int:id>", methods=["PUT"])
def update_book(id):
    """
    1. get book by id
    2. Update the book parms with new data
    3. Save it
    """
    params = request.json
    book = Book.query.get(id)
    book.name = params["book_name"]
    db.session.add(book)
    db.session.commit()
    return {"Status": "Success", "message": "Book updated"}

@app.route("/book/<int:id>",  methods=["DELETE"])
def delete_book(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return {"Status": "Success", "message": "Book deleted"}

@app.route("/book",  methods=["GET"])
def get_book_list():
    books = Book.query.filter_by().all()

    results = []
    for book in books:
        results.append({"id": book.id, "name": book.name, "published_date": book.published_date, "author": book.author})

    return {"data": results}

@app.route("/book/<int:id>",  methods=["GET"])
def get_book_by_id(id):
    book = Book.query.get(id)
    return {"id": book.id, "name": book.name, "published_date": book.published_date, "author": book.author}