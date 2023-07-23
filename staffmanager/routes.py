from flask import render_template, request, redirect, url_for
from staffmanager import app, db
from staffmanager.models import Department, Employee


@app.route("/")
def home():
    return render_template("employee.html")


@app.route("/departments")
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