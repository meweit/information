from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


class Config(object):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/information35'
    SQLALCHEMY_TRACK_MODIFITIONS = False


app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
