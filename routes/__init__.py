from flask import Blueprint

user_bp = Blueprint('user', __name__)

roulette_bp = Blueprint('roulette', __name__)

from .user_routes import *
from .roulette_routes import *