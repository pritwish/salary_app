from application.app import app, db
from datetime import date

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120))


# Table 1 : Book
# - id : int (Primary Key)
# - book_name : string 
# - author : Relationship(M2M)
# - published_date : Date
# - Category : list of strings
# - Price : float
# - publisher : Relationship(1:1)

# M-M
# Book - Author 
# B1 - A1, A2
# B2 - A2, A3
# B3 - A1, A3

# M-M
# Book - Category 
# B1 - C1, C3
# B2 - C2, C1
# B3 - C3, C1

# Book
# B1
# B2 
# B3

# Author
# A1
# A2
# A3

# Book-Author
# B1 A1
# B1 A2
# B2 A2
# B3 A3
# B3 A1
# B3 A3

book_to_author = db.Table('book_to_author',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True)
)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1200))


book_to_category = db.Table('book_to_category',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(1200))
    author = db.relationship('Author', secondary=book_to_author, lazy='subquery', backref=db.backref('author', lazy=True))
    published_date = db.Column(db.Date)
    category = db.relationship('Category', secondary=book_to_category, lazy='subquery', backref=db.backref('category', lazy=True))
    price = db.Column(db.Integer)


# Table 2 :Author
# - author_id : int (Primary Key)
# - author_name : string
# - author_bio : string

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(1200))
    author_bio = db.Column(db.String(1200))

# Table 3 : Notes
# - id : int (Primary Key)
# - book : Book (ForeignKey) 1 book can have multiple notes
# - user : Book (ForeigenKey) 1 user can have take multiple notes, for multiple books

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.Date, default=date.today())

# Sample for One-many and Many-Many relationship
# class WorkItem(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), nullable=False)
#     description = db.Column(db.String(120))

#     created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     shared_with = db.relationship('User', secondary=shared_with, lazy='subquery', backref=db.backref('user', lazy=True))

# shared_with = db.Table('shared_with',
#     db.Column('work_item_id', db.Integer, db.ForeignKey('work_item.id'), primary_key=True),
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
# )

# Using the above sample write the DB models here



# create all tables and initialize app

db.create_all()
db.init_app(app)