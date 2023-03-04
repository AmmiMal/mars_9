from flask import Flask, jsonify
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars.db")
    #app.run()
    user = User()
    # user.surname = "Scott"
    # user.name = "Ridley"
    # user.age = 21
    # user.position = "captain"
    # user.speciality = "research engineer"
    # user.address = "module_1"
    # user.email = "scott_chief@mars.org"
    # user.surname = "Vardey"
    # user.name = "Max"
    # user.age = 30
    # user.position = "pilot"
    # user.speciality = "explorer"
    # user.address = "module_2"
    # user.email = "max.var@mars.org"
    # user.surname = "Black"
    # user.name = "Bella"
    # user.age = 23
    # user.position = "captain's assistant"
    # user.speciality = "geologist"
    # user.address = "module_1"
    # user.email = "bellabla@mars.org"
    user.surname = "Armas"
    user.name = "Nill"
    user.age = 19
    user.position = "doctor"
    user.speciality = "therapist"
    user.address = "module_1"
    user.email = "doc_nill@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


if __name__ == '__main__':
    main()
