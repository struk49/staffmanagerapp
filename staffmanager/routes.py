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


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")


@app.route("/edit_department/<int:department_id>", methods=["GET", "POST"])
def edit_department(department_id):
    department = Department.query.get_or_404(department_id)
    if request.method == "POST":
        department.department_name = request.form.get("department_name")
        db.session.commit()
        return redirect(url_for("departments"))
    return render_template("edit_department.html", department=department)