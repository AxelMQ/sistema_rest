from flask import Blueprint
from .controllers.user_controller import register, get_users, verificar_transaccion

def register_routes(app):
    # app.add_url_rule('/register', view_func=user_controller.register, methods=['POST'])
    # app.add_url_rule('/users', view_func=user_controller.get_users, methods=['GET'])
    
    user_bp = Blueprint('user', __name__)

    user_bp.route('/register', methods=['POST'])(register)
    user_bp.route('/users', methods=['GET'])(get_users)
    user_bp.route('/verificar', methods=['GET'])(verificar_transaccion)


    # Registrar el Blueprint en la app Flask
    app.register_blueprint(user_bp, url_prefix='')




