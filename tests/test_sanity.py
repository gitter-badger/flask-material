def test_can_import_package():
    import flask_material


def test_can_initialize_app_and_extesion():
    from flask import Flask
    from flask_material import Bootstrap

    app = Flask(__name__)
    Bootstrap(app)
