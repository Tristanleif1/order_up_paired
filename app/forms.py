from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired
# from app import app

# # Attempting to load employees from database to pass as choices list
# with app.app_context() as app:
#     from .models import Employee
#     employees = Employee.query.all() # Query breaks
#     print(employees)

# print(dir(Employee['query']))
# print('before query', Employee.query.all())
# employee_ids = [e.id for e in employees]
# print(employee_ids)

class LoginForm(FlaskForm):
    employee_number = StringField('Employee number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class TableAssignmentForm(FlaskForm):
    tables = SelectField("Tables", coerce=int)
    servers = SelectField("Servers", coerce=int, choices=[])
    assign = SubmitField("Assign")

# def getEmployees():
#     employees = Employee.query.all() # Query breaks
#     self.servers.choices=employees
