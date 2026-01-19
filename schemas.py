from app import db
from models import User, Post
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


ma=Marshmallow()
class UserSchema(SQLAlchemyAutoSchema):
  class Meta:
    model=User
    load_instance=True
    sqla_session = db.session 
        
# Schema instances    
user_schema = UserSchema()          # for single objects
users_schema = UserSchema(many=True) # for lists of objects


class PostSchema(SQLAlchemyAutoSchema):
  class Meta:
    model=Post
    load_instance=True
    sqla_session=db.session
    
post_schema=PostSchema()
posts_schema=PostSchema(many=True)    
