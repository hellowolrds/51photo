from flask import Flask, request, render_template
from admin.admin import admin
# 导入持久化对象
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/weisheji'
# 设置这一项是每次请求结束后都会自动提交数据库中的变动
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True 

db = SQLAlchemy(app)

# 后台蓝图
app.register_blueprint(admin, url_prefix="/admin")
# 导入菜单模型
from admin.model import Menu

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
