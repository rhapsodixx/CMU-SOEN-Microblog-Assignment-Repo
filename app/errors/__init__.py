from flask import Blueprint
from app.errors import handlers

bp = Blueprint('errors', __name__)

