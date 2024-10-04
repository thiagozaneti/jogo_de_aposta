from flask import Blueprint, request, jsonify
from services.roullete_logic import Roleta
from models.models import User, Betting_House
from models.database_models import Usuario, db

roulette_bp = Blueprint('roulette', __name__)
 
@roulette_bp.route("/roleta/play/<usuario>", methods=["POST"])
def play_roulette(usuario):
    """
    End-point para jogar a roleta.

    Parâmetros:
        usuario (string): nome do usuário.
        rodadas (int): número de rodadas a serem jogadas.

    Retorna:
        JSON com os dados do usuário atualizados.
    """
    rodada_padrao = 1
    user_data = request.get_json()
    if  not user_data or 'rodadas' not in user_data:
        return jsonify({"error": "Dados inválidos ou incompletos"}), 400

    # Busca o usuário no banco de dados
    user_db = Usuario.query.filter_by(username = usuario).first()       
    if not user_db:
        return jsonify({"error": "Usuário não encontrado"}), 404
    
    # Verifica se o usuário tem saldo suficiente para jogar a roleta
    if user_db.saldo <= 0 :
        return jsonify({"error": "Saldo insuficiente para jogar a roleta"}), 400

    # Cria uma instância da classe Betting_House
    casa = Betting_House(saldo=1000)

    # Cria uma instância da classe User
    user = User(user_db_instance=user_db, rodadas=user_data['rodadas'], betting_house=casa)

    # Cria uma instância da classe Roleta
    roleta = Roleta(usuario=user, casa=casa)

    # Joga a roleta
    roleta.rolar_roleta(rodadas=user.rodadas)

    # Retorna os dados do usuário atualizados
    return jsonify({
        "rodadas": user.rodadas,
        "saldo_final": user.saldo,
        "ganhos": user.ganhos,
        "derrotas": user.derrotas,
        "layout_grid":user.layout_grid
    })


