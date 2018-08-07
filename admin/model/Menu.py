from app import db

class Menu(db.Model):
  __tablename__  = 'menu'

  id = db.Column(db.Integer, primary_key=True)
  parent_id = db.Column(db.Integer)
  icon = db.Column(db.String(50))
  menu_name = db.Column(db.String(60))
  created_at = db.Column(db.Integer)
  menu_name = db.Column(db.String(60))
  status = db.Column(db.Integer)