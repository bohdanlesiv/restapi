from models.user import UserModel
from werkzeug.security import  safe_str_cmp


def authenticate(username, password):
    user = UserModel.find_by_user_name(username)
    if user and safe_str_cmp(user.password,password):
        return user

def identity(payload):
    userid= payload.get('identity')
    return UserModel.find_user_by_id(userid)

