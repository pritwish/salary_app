from application.app import app, db
from datetime import date

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(120))


# Table 1: salary
# - salary_id - int (Primary key)
# - salary : int
# - salary_currency : string
# - company : Relationship(M2M)
# - designation : Relationship(M2M)
# - YoE : int
# - number_of_data : Relationship(1:1)

salary_to_company = db.Table('salary_to_company',
    db.Column('salary_id', db.Integer, db.ForeignKey('salary.id'), primary_key=True),
    db.Column('company_id', db.Integer, db.ForeignKey('company.id'), primary_key=True)
)

salary_to_designation = db.Table('salary_to_designation',
    db.Column('salary_id', db.Integer, db.ForeignKey('salary.id'), primary_key=True),
    db.Column('designation_id', db.Integer, db.ForeignKey('designation.id'), primary_key=True)
)

class Salary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    salary = db.Column(db.Integer, nullable=True)
    salary_currency = db.Column(db.String(50))
    company = db.relationship('Company', secondary= salary_to_company, lazy='subquery', backref=db.backref('salary', lazy=True))
    designation = db.relationship('Designation', secondary= salary_to_designation, lazy='subquery', backref=db.backref('salary', lazy=True))
    YoE = db.Column(db.Integer, nullable=True)
    # number_of_data = 
    


# Table 2 : Company
# - company_id : int (Primary_key)
# - company_name : string
# - company_strength : int

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(500))
    company_strength = db.Column(db.Integer)



# Table 3: Designation
# - designation_name : string
# - designation_id : int (Primary key)

class Designation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    designation_name = db.Column(db.Integer)

# Table 4: datapoints
# - number_of_datapoints : int
# - datapoint_id : int (Primary key)
# - Date - date
class datapoints(db.Model):
    no_data = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)

# class Datapoints(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     number_of_datapoints = db.Column(db.Integer)
#     date_entry = db.Column(db.Date, default=date.today())




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