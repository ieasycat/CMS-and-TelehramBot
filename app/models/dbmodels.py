from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class Manager(db.Model):
    __tablename__ = 'manager'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.email}>'


class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    nickname = db.Column(db.String(50))
    main_technology = db.Column(db.String(50))
    status = db.Column(db.String(15))
    employee_data = db.relationship(
        'EmployeeData',
        backref='employee',
        uselist=False,
        cascade="all, delete-orphan",
        single_parent=True
    )

    def generate_nickname(self):
        self.nickname = f'{self.main_technology}_{self.id}'

    def change_status(self):
        if self.status == 'Free':
            self.status = 'Busy'
        else:
            self.status = 'Free'

    def __repr__(self):
        return f'<User {self.nickname}>'


class EmployeeData(db.Model):
    __tablename__ = 'employee_data'
    id = db.Column(db.Integer, primary_key=True)
    cv = db.Column(db.Text, nullable=True)
    additional_data = db.Column(db.Text, nullable=True)
    employee_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'employee.id',
            ondelete="CASCADE"
        ),
    )

    def __repr__(self):
        return f'<User {self.employee_id}>'
