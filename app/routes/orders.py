from flask import Blueprint, render_template
from flask_login import login_required
from app.forms import TableAssignmentForm
from app.models import Employee, Table

bp = Blueprint("orders", __name__, url_prefix="")


@bp.route("/", methods=['GET', 'POST'])
@login_required
def index():
    orderForm = TableAssignmentForm()
    tables = Table.query.all()
    # print(employees)
    # print(tables)
    # employees = Employee.query.all()
    # employee_names = [e.name for e in employees]
    orderForm.tables.choices = [t.id for t in tables]

    # table_ids = [t.id for t in tables]
    return render_template('orders.html', form=orderForm)
