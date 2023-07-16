from staffmanager import db


class Department(db.Model):
    # Schema for the department  model
    id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(30), unique=True, nullable=False)
    employee = db.relationship("Employee", backref="department", cascade="all, delete", lazy=True)


    def __repr__(self):
        #__repr__ to represent itself in a form of a string
        return self.department_name

        
class Employee(db.Model):
    # Schema for the employee model
    id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(50), unique=True, nullable=False)
    # employee_description = db.column(db.text, nullable=False)
    employee_email = db.Column(db.String(150), unique=True, nullable=False)
    employee_position = db.Column(db.String(20), unique=True, nullable=False)
    employee_skills = db.Column(db.String(50), unique=True, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    
    department_id = db.Column(db.Integer, db.ForeignKey("department.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        #__repr__ to represent itself in a form of a string
        return "#{0} - Employee: {1} | Skills: {2}".format(
            self.id, self.employee_name, self.employee_skills
        )