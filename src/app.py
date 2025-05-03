from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Usuario, Personaje, Planeta, Favorito

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Ruta de prueba
@app.route('/')
def home():
    return jsonify({"mensaje": "Bienvenido al blog de Star Wars"})

# Obtener todos los personajes
@app.route('/personajes', methods=['GET'])
def get_personajes():
    personajes = Personaje.query.all()
    return jsonify([{"id": p.id, "nombre": p.nombre, "descripcion": p.descripcion} for p in personajes])

# Agregar un nuevo personaje
@app.route('/personajes', methods=['POST'])
def add_personaje():
    data = request.get_json()
    nuevo_personaje = Personaje(nombre=data['nombre'], descripcion=data['descripcion'])
    db.session.add(nuevo_personaje)
    db.session.commit()
    return jsonify({"mensaje": "Personaje agregado correctamente"}), 201

# Obtener todos los planetas
@app.route('/planetas', methods=['GET'])
def get_planetas():
    planetas = Planeta.query.all()
    return jsonify([{"id": p.id, "nombre": p.nombre, "clima": p.clima, "terreno": p.terreno} for p in planetas])

# Crear contexto para la base de datos
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
