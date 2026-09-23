import os
from flask import Flask
from flask_login import LoginManager

from .extensions import db
from .models import User

login_manager = LoginManager()
login_manager.login_view = "auth.login"


def create_app():
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
    )
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-change-me")

    db_url = os.environ.get("DATABASE_URL", "sqlite:///storeline.db")
    if db_url.startswith("postgres://"):
        # Render (and some providers) hand out the old-style scheme;
        # SQLAlchemy 1.4+/2.x needs postgresql://
        db_url = db_url.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    login_manager.init_app(app)

    from .auth import auth_bp
    from .admin_routes import admin_bp
    from .store_routes import store_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(store_bp)

    with app.app_context():
        db.create_all()
        from .seed import seed_if_empty
        seed_if_empty()

    return app


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
