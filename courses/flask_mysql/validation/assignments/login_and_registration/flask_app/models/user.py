from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
from flask_app import app
from flask import flash
import re
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    DB = "login_and_registration"

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def register(cls, user_data):
        data = {
            "first_name" : user_data["first_name"],
            "last_name" : user_data["last_name"],
            "email" : user_data["email"],
            "password" : bcrypt.generate_password_hash(user_data["password"])
        }
        query = """
                INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
                """
        id = connectToMySQL(cls.DB).query_db(query, data)
        print("__REGISTER__", id)
        return id

    @classmethod
    def get_by_id(cls,id):
        data = {"id" : id}
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        return cls(results[0])

    @classmethod
    def get_by_email(cls, email):
        data = {"email" : email}
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        if len(results) == 0:
            return False
        else:
            return cls(results[0])

    @staticmethod
    def validate_login(user):
        is_valid = True
        if not user["email"] or not EMAIL_REGEX.match(user["email"]):
            flash("Invalid email address!","login")
            is_valid = False
        user_in_db = User.get_by_email(user["email"])
        print("@@@ARE WE HERE?@@@")
        if user_in_db is False:
            flash("Wrong Email / Password", "login")
            is_valid = False
        else:
            print("__LOOK HERE___", bcrypt.check_password_hash(user_in_db.password, user["password"]))
            if len(user["password"]) <= 7 or not bcrypt.check_password_hash(user_in_db.password, user["password"]):
                flash("Wrong Email / Password", "login")
                is_valid = False
            if is_valid:
                return user_in_db
            else:
                is_valid

    @staticmethod
    def validate_register(user):
        is_valid = True
        user_in_db = User.get_by_email(user["email"])
        print("__USER IN DB__", user_in_db)
        if not user["first_name"] or len(user["first_name"]) < 2:
            flash("First Name must be at least 2 characters!", "register")
            is_valid = False
        if not user["last_name"] or len(user["last_name"]) < 2:
            flash("Last Name must be at least 2 characters!", "register")
            is_valid = False
        if not user["email"] or not EMAIL_REGEX.match(user["email"]):
            flash("Invalid email address!", "register")
            is_valid = False
        if user_in_db is not False:
            flash("User already exists!", "register")
            is_valid = False
        if not user["password"] or len(user["password"]) <= 7:
            flash("Password must be at least 8 characters!", "register")
            is_valid = False
        if not user["confirm_password"] or user["password"] != user["confirm_password"]:
            flash("Password must match!", "register")
            is_valid = False
        return is_valid