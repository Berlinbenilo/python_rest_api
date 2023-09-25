from flask import Blueprint

auth = Blueprint("auth", __name__, url_prefix='/api/v1/auth')


@auth.get('/me')
def me():
    return {"message": "me"}


@auth.post('/register')
def register():
    return {"message": "user created"}