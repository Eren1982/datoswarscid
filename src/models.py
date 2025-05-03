from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    favoritos = db.relationship('Favorito', back_populates='usuario')

class Personaje(db.Model):
    __tablename__ = 'personaje'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255))
    favoritos = db.relationship('Favorito', back_populates='personaje')

class Planeta(db.Model):
    __tablename__ = 'planeta'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    clima = db.Column(db.String(100))
    terreno = db.Column(db.String(100))
    favoritos = db.relationship('Favorito', back_populates='planeta')

class Favorito(db.Model):
    __tablename__ = 'favorito'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    personaje_id = db.Column(db.Integer, db.ForeignKey('personaje.id'), nullable=True)
    planeta_id = db.Column(db.Integer, db.ForeignKey('planeta.id'), nullable=True)

    usuario = db.relationship('Usuario', back_populates='favoritos')
    personaje = db.relationship('Personaje', back_populates='favoritos')
    planeta = db.relationship('Planeta', back_populates='favoritos')
