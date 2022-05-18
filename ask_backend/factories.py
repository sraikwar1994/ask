from flask import Flask


def test_app():
    test_app = Flask(__name__)
    config = "ask_backend.config.TestingConfig"
    test_app.config.from_object(config)
    test_db = SQLAlchemy(test_app)
    test_db.init_app(app)
    Migrate(app, test_db)
