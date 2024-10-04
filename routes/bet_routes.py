from flask import Blueprint, request, jsonify
from services.roullete_logic import Roleta
from models.models import User, Betting_House
from models.database_models import Usuario, db

bet_bp = Blueprint('bet', __name__)

@bet_bp.route("/bank", methods=["GET"])
def bet():
    casa = Betting_House(saldo=10000)
    return jsonify({"saldo":casa.saldo_casa})