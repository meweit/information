from flask import Flask, session
from flask.ext.migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis
from flask_session import Session


class Config(object):
    # 配置Secret_key
    SECRET_KEY = '3fxmHberuyFpzJkgZplyuFCpy7aLfhz0ytkzHtyHfQxw1a4rqv7432kz4h3WFQ/+'
    # 项目配置
    DEBUG = True
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/information35'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # redis配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    # Session 保存配置
    SESSION_TYPE = 'redis'
    # 开启Session签名
    SESSION_USE_SIGNER = True
    # 指定Session保存的redis
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 开启过期
    SESSION_PERMANENT = False
    # 设置过期时间　单位：秒
    PERMANENT_SESSION_LIFETIME = 86480 * 2


app = Flask(__name__)
# 加载配置
app.config.from_object(Config)
# 初始化数据库
db = SQLAlchemy(app)
# 初始化redis存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启CSRF 保护
CSRFProtect(app)
# 设置session保存指定位置
Session(app)

manager = Manager(app)
# 将app与db 关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)

@app.route('/')
def index():
    session['name'] = 'hello python'
    return 'index'


if __name__ == '__main__':
    manager.run()
