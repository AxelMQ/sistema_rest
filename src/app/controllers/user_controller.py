from flask import request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import scoped_session
from ..models import User
import uuid
from ..db import SessionLocal

def register():
    session = SessionLocal() # Obtener instancia de sesion
    try:
        data = request.get_json()
        nombre = data.get('nombre')
        apellido = data.get('apellido')
        direccion = data.get('direccion')
        fecha_nac = data.get('fecha_nac')
        estado_civil = data.get('estado_civil')

        # Verificar que los datos requeridos estén presentes
        if not nombre or not apellido or not direccion or not fecha_nac or not estado_civil:
            return jsonify({
                "error": "Todos los campos son obligatorios"
            }), 400
        
        # Generar una transaccion_id unico
        # transaccion_id = str(uuid.uuid4())

        # existe_transaccion = session.query(User).filter_by(transaccion_id=transaccion_id).first()
        # if existe_transaccion:
        #     return jsonify({
        #         "error": "Esta transaccion ya fue procesada."
        #     }), 400
        
        # Registramos al nuevo usuario
        usuario = User(
            nombre=nombre,
            apellido=apellido,
            direccion=direccion,
            fecha_nac=fecha_nac,
            estado_civil=estado_civil,
            # transaccion_id=transaccion_id
        )

        # Añadir el nuevo usuario a la BD
        session.add(usuario)
        session.commit() # Confirmar la transaccion

        # Responder con exito los datos registrados
        return jsonify({
            "message": "Datos del Usuario Registrado con exito", 
            "usuario": usuario.to_dict(),
            "transaccion_id": usuario.transaccion_id
        }), 201

    
    except SQLAlchemyError as e:
        session.rollback()  # Revertir cualquier cambio en caso de error
        return jsonify({"error": "Ocurrió un error al intentar registrar el usuario", "detalle": str(e)}), 500
    
    except Exception as e:
        return jsonify({"error": "Ocurrió un error inesperado", "detalle": str(e)}), 500

    finally:
        session.close()  # Cerrar la sesión de la base de datos

def verificar_transaccion():
    session = SessionLocal()
    try:
        # Obtenemos la transaccion_id del request
        transaccion_id = request.args.get('transaccion_id')

        if not transaccion_id:
            return jsonify({"error": "transaccion_id es requerido"}), 400

        # Buscamos al usuario asociado con el transaccion_id
        usuario = session.query(User).filter_by(transaccion_id=transaccion_id).first()

        if not usuario:
            return jsonify({"error": "Transacción no encontrada"}), 404

        # Devolvemos la información del usuario si se encuentra
        return jsonify({
            "message": "Transacción encontrada",
            "usuario": usuario.to_dict()
        }), 200

    except SQLAlchemyError as e:
        return jsonify({"error": "Error al verificar la transacción", "detalle": str(e)}), 500

    except Exception as e:
        return jsonify({"error": "Error inesperado", "detalle": str(e)}), 500

    finally:
        session.close()

def get_users():
    session = SessionLocal() # Obtener instancia de sesion
    try:
        usuarios = session.query(User).all()
        return jsonify([usuario.to_dict() for usuario in usuarios]), 200

    except SQLAlchemyError as e:
        return jsonify({
            "error": "Ocurrió un error al intentar obtener los usuarios", 
            "detalle": str(e)
        }), 500

    except Exception as e:
        return jsonify({
            "error": "Ocurrió un error inesperado", 
            "detalle": str(e)
        }), 500

    finally:
        session.close()  # Cerrar la sesión de la base de datos