from flask import Flask, jsonify
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars.db")
    app.run()


if __name__ == '__main__':
    main()
