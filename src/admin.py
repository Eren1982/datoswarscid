from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import app, db
from models import Usuario, Personaje, Planeta, Favorito

admin = Admin(app, name="Administración", template_mode="bootstrap3")
admin.add_view(ModelView(Usuario, db.session))
admin.add_view(ModelView(Personaje, db.session))
admin.add_view(ModelView(Planeta, db.session))
admin.add_view(ModelView(Favorito, db.session))

if __name__ == "__main__":
    app.run(debug=True)
