from application.app import app, db
from flask import request
import sqlalchemy
# Import your models here
from application.models import Salary, Company, Designation
# from flask_jwt import jwt_required, JWT, current_identity

# def identity(payload):
#     user_id = payload['identity']
#     return User.query.filter_by(id=user_id).first()

# def authenticate(username, password):
#     user = User.query.filter_by(username=username).first()
#     if user and user.password == password:
#         return user

# jwt = JWT(app, authenticate, identity)

# @app.route("/signup", methods=["POST"])
# def signup():
#     params = request.json
#     try:
#         user = User(**params)
#         db.session.add(user)
#         db.session.commit()
#     except sqlalchemy.exc.IntegrityError:
#         return {"Status": "Error", "result": "User already exists"}, 400
#     return {"Status": "Success", "result": "User created"}

# @app.route("/")
# @jwt_required()
# def home():
#     return {"Status": "Success", "username": current_identity.username}, 200 
@app.route("/")
def home():
    return {"Status":"Success"}, 200

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


# 1. list all salaries - GET - salary - /salary
# 2. add salary - POST - salary - /salary
# 3. delete salary - DELETE - /salary/{id}
# 4. update salary - PUT -/salary/{id}
# 5. get salary by designation - GET - /salary/{id}/designation
# 6. get salary by company name - GET
# 7. get salary by years of experience - GET

@app.route("/salary", methods=["POST"])
def add_salary():
    params = request.json
    salary = Salary(salary=params["salary"], salary_currency=params["salary_currency"])
    db.session.add(salary)
    db.session.commit()
    return {"id": salary.id, "salary currency":salary.salary_currency, "salary":salary.salary}

@app.route("/salary/<int:id>", methods=["PUT"])
def update_salary(id):
    params = request.json
    salary = Salary.query.get(id)
    salary.salary_currency = params["salary_currency"]
    salary.salary = params["salary"]
    salary.YoE = params["YoE"]
    db.session.add(salary)
    db.session.commit()
    return {"Status":"success","message":"salary updated"}

@app.route("/salary/<int:id>", methods=["GET"])
def get_salary_by_id(id):
    salary = Salary.query.get(id)
    return {"id": salary.id, "salary currency":salary.salary_currency, "salary":salary.salary}

@app.route("/salary/<int:id>", methods=["DELETE"])
def delete_salary(id):
    salary = Salary.query.get(id)
    db.session.delete(salary)
    db.session.commit()
    return {"Status":"success","message":"salary deleted"}

@app.route("/salary", methods=["GET"])
def get_salary_list():
    salarys = Salary.query.filter_by().all()

    results = []
    for salary in salarys:
        results.append({"id": salary.id, "salary currency":salary.salary_currency, "salary":salary.salary})
    return {"data":results}




# @app.route("/salary/<company>", methods=["GET"])
# def get_salary_by_company(company):
#     pass



# @app.route("/book", methods=["POST"])
# def add_book():
#     # name, author, pages
#     params = request.json
#     book = Book(name=params["book_name"])
#     category_ids = params.get("categories", [])
#     for c_id in category_ids:
#         category = Category.query.get(c_id)
#         if category:
#             book.category.append(category)

#     author_ids = params.get("author_ids", [])
#     for a_id in author_ids:
#         author = Author.query.get(a_id)
#         if author:
#             book.author.append(author)


#     db.session.add(book)
#     db.session.commit()


#     return {"id": book.id, "name": book.name, "published_date": book.published_date, 
#             "author": [author.id for author in book.author], 
#             "category": [category.id for category in book.category]}

# @app.route("/book/<int:id>", methods=["PUT"])
# def update_book(id):
#     """
#     1. get book by id
#     2. Update the book parms with new data
#     3. Save it
#     """
#     params = request.json
#     book = Book.query.get(id)
#     book.name = params["book_name"]
#     db.session.add(book)
#     db.session.commit()
#     return {"Status": "Success", "message": "Book updated"}

# @app.route("/book/<int:id>",  methods=["DELETE"])
# def delete_book(id):
#     book = Book.query.get(id)
#     db.session.delete(book)
#     db.session.commit()
#     return {"Status": "Success", "message": "Book deleted"}

# @app.route("/book",  methods=["GET"])
# def get_book_list():
#     books = Book.query.filter_by().all()

#     results = []
#     for book in books:
#         results.append({"id": book.id, "name": book.name, "published_date": book.published_date, "author": book.author})

#     return {"data": results}

# @app.route("/book/<int:id>",  methods=["GET"])
# def get_book_by_id(id):
#     book = Book.query.get(id)
#     return {"id": book.id, "name": book.name, "published_date": book.published_date, "author": book.author}


# @app.route("/book/<int:book_id>/note", methods=["POST"])
# @jwt_required()
# def add_note(book_id):
#     book = Book.query.get(book_id)
#     if not book:
#         return {"status": "Error"}, 401

#     params = request.json
#     note = Notes(note=params["note"], book=book_id, created_by=current_identity.id)
#     db.session.add(note)
#     db.session.commit()
#     return {"id": note.id, "note": note.note, "created_at": note.created_at, "created_by": note.created_by}
    

# @app.route("/book/<int:book_id>/note", methods=["GET"])
# def get_all_notes(book_id):
#     notes = Notes.query.filter_by(book=book_id).all()
#     results = []

#     for note in notes:
#         results.append({"id": note.id, "note": note.note, "created_at": note.created_at})

#     return {"data": results}

# @app.route("/book/<int:book_id>/note/<int:note_id>", methods=["GET"])
# def get_note_by_id(book_id, note_id):
#     note = Notes.query.get(note_id)
#     return {"id": note.id, "note": note.note, "created_at": note.created_at}
    

# @app.route("/author", methods=["POST"])
# def add_author():
#     # name, author, pages
#     params = request.json
#     author = Author(author_name=params["name"], author_bio=params.get("bio"))
#     db.session.add(author)
#     db.session.commit()
#     return {"id": author.id, "name": author.author_name, "bio": author.author_bio}

# @app.route("/category", methods=["POST"])
# def add_category():
#     # name, author, pages
#     params = request.json
#     category = Category(name=params["name"])
#     db.session.add(category)
#     db.session.commit()
#     return {"id": category.id, "name": category.name}


# @app.route("/author",  methods=["GET"])
# def get_author_list():
#     authors = Author.query.filter_by().all()

#     results = []
#     for author in authors:
#         results.append({"id": author.id, "name": author.author_name, "bio": author.author_bio})

#     return {"data": results}

# @app.route("/category",  methods=["GET"])
# def get_category_list():
#     categories = Category.query.filter_by().all()

#     results = []
#     for category in categories:
#         results.append({"id": category.id, "name": category.name})

#     return {"data": results}