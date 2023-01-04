from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
from flask_app import app
import re
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    DB = "belt_review"

    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def register(cls,user_data):
        data = {
            "first_name":user_data["first_name"],
            "last_name":user_data["last_name"],
            "email":user_data["email"],
            "password":bcrypt.generate_password_hash(user_data["password"])
        }

        query = """
                INSERT INTO users (first_name,last_name,email,password) VALUES
                (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
                """
        id = connectToMySQL(cls.DB).query_db(query,data)
        print("__REGISTER__",id)
        return id

    @classmethod
    def get_by_email(cls,email):
        data = {"email":email}
        query = "SELECT * FROM users WHERE email=%(email)s;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        if len(results) == 0:
            return False
        else:
            return cls(results[0])

    @staticmethod
    def validate_register(user):

        is_valid = True
        user_in_db = User.get_by_email(user["email"])
        if
        return is_valid