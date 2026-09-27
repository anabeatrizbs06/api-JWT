from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

from database.db import db
from models.user_model import User


class UserController:

    @staticmethod
    def register_user(data):

        nome = data.get("nome")
        email = data.get("email")
        senha = data.get("senha")

        if not nome or not email or not senha:
            return {
                "erro": "Nome, email e senha são obrigatórios"
            }, 400

        usuario_existente = User.query.filter_by(
            email=email
        ).first()

        if usuario_existente:
            return {
                "erro": "Email já cadastrado"
            }, 409

        senha_hash = generate_password_hash(senha)

        novo_usuario = User(
            nome=nome,
            email=email,
            senha=senha_hash
        )

        db.session.add(novo_usuario)
        db.session.commit()

        return {
            "mensagem": "Usuário criado com sucesso",
            "usuario": novo_usuario.to_dict()
        }, 201

    @staticmethod
    def login_user(data):

        email = data.get("email")
        senha = data.get("senha")

        if not email or not senha:
            return {
                "erro": "Email e senha são obrigatórios"
            }, 400

        usuario = User.query.filter_by(
            email=email
        ).first()

        if not usuario:
            return {
                "erro": "Email ou senha inválidos"
            }, 401

        if not check_password_hash(
            usuario.senha,
            senha
        ):
            return {
                "erro": "Email ou senha inválidos"
            }, 401

        access_token = create_access_token(
            identity=str(usuario.id)
        )

        return {
            "access_token": access_token
        }, 200

    @staticmethod
    def get_user(user_id):

        usuario = User.query.get(user_id)

        if not usuario:
            return {
                "erro": "Usuário não encontrado"
            }, 404

        return usuario.to_dict(), 200

    @staticmethod
    def update_user(user_id, data):

        usuario = User.query.get(user_id)

        if not usuario:
            return {
                "erro": "Usuário não encontrado"
            }, 404

        if "nome" in data:
            usuario.nome = data["nome"]

        if "email" in data:

            email_existente = User.query.filter(
                User.email == data["email"],
                User.id != user_id
            ).first()

            if email_existente:
                return {
                    "erro": "Email já cadastrado"
                }, 409

            usuario.email = data["email"]

        if "senha" in data:
            usuario.senha = generate_password_hash(
                data["senha"]
            )

        db.session.commit()

        return {
            "mensagem": "Usuário atualizado com sucesso",
            "usuario": usuario.to_dict()
        }, 200

    @staticmethod
    def delete_user(user_id):

        usuario = User.query.get(user_id)

        if not usuario:
            return {
                "erro": "Usuário não encontrado"
            }, 404

        db.session.delete(usuario)
        db.session.commit()

        return {
            "mensagem": "Usuário excluído com sucesso"
        }, 200