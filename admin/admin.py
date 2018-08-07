from flask import Blueprint, render_template, request

admin = Blueprint('admin', __name__, template_folder='template', static_folder='static')

from admin.model import Menu
# from app import db

@admin.route('/index')
def index ():
  return render_template('index/index.html')

@admin.route('/test')
def test ():
  # data = Menu.query.all()
  print(Menu)
  return 'test'

