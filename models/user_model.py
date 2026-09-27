from database.db import db


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(150),
        unique=True,
        nullable=False
    )

    senha = db.Column(
        db.String(255),
        nullable=False
    )

    formularios = db.relationship(
        "Formulario",
        backref="usuario",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def to_dict(self):

        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email
        }