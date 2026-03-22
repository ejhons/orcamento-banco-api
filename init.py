from main import app
from extensions import db


def init_banco():
    with app.app_context():
        db.drop_all()
        db.create_all()


if __name__ == 'main':
    init_banco()
