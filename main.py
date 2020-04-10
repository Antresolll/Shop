from data import db_session
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    app.run()
    db_session.global_init("db/blogs.sqlite")


if __name__ == '__main__':
    main()
