from flask import request, jsonify
from werkzeug.exceptions import NotFound, BadRequest
from app import db, app
from models import User,Post
from schemas import user_schema,users_schema,post_schema,posts_schema
from flask_jwt_extended import jwt_required, get_jwt_identity



@app.post("/register")
def register():
    data = request.get_json()
    if not data:
        return NotFound("Missing or invalid data!"), 404

    # Deserialize JSON into a User instance
    user = user_schema.load(data)

    try:
        user.set_email(email=user.email)  
    except ValueError as e:
        return jsonify(message=str(e)), 400

    user.set_password(password=user.password)  #

    db.session.add(user)
    db.session.commit()

    return jsonify(message="User registered successfully!"), 201
  
  
@app.post("/login")
def login():
  data= request.get_json()
  if not data:
    raise BadRequest("Invalid data!.")
  email=data["email"]
  password=data['password']
  
  token,_ =User.authenticate(email, password)
  if not token:
    raise NotFound("Invalid credentail!.")
  
  return jsonify(
            access_token= token)
  
 
@app.post("/add")
@jwt_required()
def add_post():
  data=request.get_json()
  if not data:
    raise BadRequest("Missing or Invalid data")
  title=data['title']
  body=data['body']
  author_id=get_jwt_identity()
  db.session.add(Post(title= title, body=body ,author_id=author_id))
  db.session.commit()
  return jsonify(message="Post added successfully!.")
 
 
  
@app.get("/posts")
def get_posts():
  posts=Post.query.all()
  if not posts:
    return jsonify(message="Post doesn't exists!.")
  return jsonify( posts_schema.dump(posts))
  
  
@app.get("/post/<int:post_id>")
def get_1(post_id):
  post=Post.query.filter_by(id=post_id).first()
  if not post:
    return  {"message": "Post not exists!."}
  return jsonify(post_schema.dump(post))  
  
  
  
@app.patch("/post/<int:post_id>")
@jwt_required()
def update(post_id):
  post=Post.query.filter_by(id=post_id).first()
  if not post:
    return  {"message": "Post not exists!."}
  author_id=get_jwt_identity()
  data=request.get_json()
  if not data:
    return jsonify(message="Messing or Invalid data!.")
  
  post.title=data['title']
  post.body=data['body']
 
  db.session.commit()
  return jsonify(message="Post updated!.")
  

@app.delete("/post/<int:post_id>")
@jwt_required()
def delete(post_id):
  post=Post.query.filter_by(id=post_id).first()
  if not post:
    return  {"message": "Post not exists!."}
  author_id=get_jwt_identity()
  if post.author_id != author_id:
    return jsonify(message="You are not authorized to delete this post"), 403


  db.session.delete(post)
  db.session.commit()
  
  return jsonify(message="Post deleted!.")
  
  
  
  
  
  
  
  