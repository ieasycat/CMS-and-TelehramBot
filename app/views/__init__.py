from flask import Blueprint

main = Blueprint('main', __name__)
bp = Blueprint('employee', __name__)

from app.views import view
