from app import db
from datetime import datetime
from email_validator import validate_email,EmailNotValidError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
 
 
 
class User(db.Model):
  __tablename__="users"
  id=db.Column(db.Integer, primary_key=True)
  username=db.Column(db.String(50), nullable=False,unique=True, index=True)
  email=db.Column(db.String(250), unique=True, index=True, nullable=False)
  password=db.Column(db.String(200))
  timestamp=db.Column(db.DateTime, index=True, default=datetime.utcnow())
  posts=db.relationship("Post", backref="author", lazy="dynamic")
  def set_email(self, email):
    try:
      valid=validate_email(email)
      self.email=valid.email
    except EmailNotValidError as e:
      raise ValueError(f"Email invalid: {str(e)}!.")
    
  def set_password(self, password):
    self.password=generate_password_hash(password)
    
  def check_password(self, password):
    return check_password_hash(self.password, password)
  
  @classmethod
  def authenticate(cls, email, password):
    user=User.query.filter_by(email=email).first()
    if user and user.check_password(password):
      access_token= create_access_token(identity=str(user.id))
      return access_token, user
    

class Post(db.Model):
  __tablename__="posts"
  id=db.Column(db.Integer, primary_key=True)
  title=db.Column(db.String(80), index=True, nullable=False)
  body=db.Column(db.Text,nullable=False)
  timestamp=db.Column(db.DateTime, index=True, default=datetime.utcnow())
  author_id=db.Column(db.Integer, db.ForeignKey("users.id"))    
    