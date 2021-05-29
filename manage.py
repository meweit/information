from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis


class Config(object):
    # 项目配置
    DEBUG = True
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/information35'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # redis配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379


app = Flask(__name__)
# 加载配置
app.config.from_object(Config)
# 初始化数据库
db = SQLAlchemy(app)
# 初始化redis存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启CSRF 保护
CSRFProtect(app)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
