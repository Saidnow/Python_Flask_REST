from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
import datetime

from security import autenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store,StoreList
from db import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///mydatabase.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "/said1234"
api = Api(app)


#to avoid fast expiration of secet key of athentification jwt
#JWT configuration

app.config["JWT_EXPIRATION_DELTA"] = datetime.timedelta(minutes=10)
#app.config["JWT_AUTH_URL_RULE"] = '/login'  #to change the default authentification url "/auth"
#app.config["JWT_AUTH_USERNAME_KEY"] = 'email' # username by default or email if we changed is the case here :,)
jwt = JWT(app,autenticate,identity) # /auth by default or /login if we changed above



api.add_resource(Store, "/store/<string:name>")
api.add_resource(Item, "/item/<string:name>") #http://127.0.0.1:5000/student/Rolf
api.add_resource(ItemList, "/items")
api.add_resource(StoreList, "/stores")

api.add_resource(UserRegister, "/register")

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000,debug=True)
