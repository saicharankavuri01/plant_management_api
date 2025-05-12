from flask import Flask
from app.config import Config
from app.extensions import db, migrate  # ✅ import from extensions
from app.routes.work_order import bp as work_order_bp
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(work_order_bp)

    return app
