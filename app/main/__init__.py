from flask import Blueprint
# defining our Blueprint
main = Blueprint('main',__name__)
from app import views, errors