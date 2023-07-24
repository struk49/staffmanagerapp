from flask import render_template, request, redirect, url_for
from staffmanager import app, db
from staffmanager.models import Department, Employee


@app.route("/")
def home():
    employees = list(Employee.query.order_by(Employee.id).all())
    return render_template("employee.html", employees=employees)


@app.route("/department")
def departments():
    departments = list(Department.query.order_by(Department.department_name).all())
    return render_template("departments.html", departments=departments)


@app.route("/add_department", methods=["GET", "POST"])
def add_department():
    if request.method == "POST":
        department = Department(department_name=request.form.get("department_name"))
        db.session.add(department)
        db.session.commit()
        return redirect(url_for("departments"))
    return render_template("add_department.html")


@app.route("/edit_department/<int:department_id>", methods=["GET", "POST"])
def edit_department(department_id):
    department = Department.query.get_or_404(department_id)
    if request.method == "POST":
        department.department_name = request.form.get("department_name")
        db.session.commit()
        return redirect(url_for("departments"))
    return render_template("edit_department.html", department=department)


@app.route("/delete_department/<int:department_id>")
def delete_department(department_id):
    department = Department.query.get_or_404(department_id)
    db.session.delete(department)
    db.session.commit()
    return redirect(url_for("departments"))


@app.route("/add_employee", methods=["GET", "POST"])
def add_employee():
    departments = list(Department.query.order_by(Department.department_name).all())
    if request.method == "POST":
        employee = Employee(
            employee_name=request.form.get("employee_name"),
            employee_email=request.form.get("employee_email"),
            employee_position=request.form.get("employee_position"),
            employee_skills=request.form.get("employee_skilss"),
            start_date=request.form.get("start_date"),
            deaprtment_id=request.form.get("deaprtment_id")
        )
        db.session.add(employee)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_employee.html", departments=departments)


@app.route("/edit_employee/<int:employee_id>", methods=["GET", "POST"])
def edit_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    department = list(Department.query.order_by(Department.department_name).all())
    if request.method == "POST":
        employee.employee_name = request.form.get("employee_name")
        employee.employee_email = request.form.get("employee_email")
        employee.start_date = request.form.get("start_date")
        employee.department_id = request.form.get("department_id")
        db.session.commit()
    return render_template("edit_employee.html", employee=employee, departments=departments)


@app.route("/delete_employee/<int:employee_id>")
def delete_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for("home"))