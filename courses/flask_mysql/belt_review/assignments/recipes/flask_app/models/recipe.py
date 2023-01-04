from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from flask_app.models import user

class Recipe:
    DB = "recipes"

    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.date_made = data["date_made"]
        self.under_30 = data["under_30"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.creator = None

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if not recipe["name"] or len(recipe["name"]) < 3:
            flash("Name must be at least 3 characters!")
            is_valid = False
        if not recipe["description"] or len(recipe["description"]) < 3:
            flash("Description must be at least 3 characters!")
            is_valid = False
        if not recipe["instructions"] or len(recipe["instructions"]) < 3:
            flash("Instructions must be at least 3 characters!")
            is_valid = False
        if not recipe["date_made"] or len(recipe["date_made"]) <= 0:
            flash("Date is required.")
            is_valid = False
        if "under_30" not in recipe:
            flash("Does your recipe take less than 30 min?")
            is_valid = False
        return is_valid

    @classmethod
    def create_recipe(cls,data):
        query = """
                INSERT INTO recipes (name,description,instructions,date_made,under_30,user_id)
                VALUES (%(name)s,%(description)s,%(instructions)s,%(date_made)s,%(under_30)s,%(user_id)s);
                """
        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def get_all_recipes(cls):
        query = """
                SELECT * FROM recipes JOIN users ON recipes.user_id = users.id
                ORDER BY recipes.created_at
                """
        results = connectToMySQL(cls.DB).query_db(query)
        recipes = []
        for row in results:
            recipe = cls(row)
            recipe_creator_info = {
                "id":row["users.id"],
                "first_name":row["first_name"],
                "last_name":row["last_name"],
                "email":row["email"],
                "password":row["password"],
                "created_at":row["users.created_at"],
                "updated_at":row["users.updated_at"]
            }
            creator = user.User(recipe_creator_info)
            recipe.creator = creator
            recipes.append(recipe)
        return recipes

    @classmethod
    def get_recipe(cls,recipe_id):
        data = {"id":recipe_id}
        query = """
                SELECT * FROM recipes JOIN users ON recipes.user_id = users.id
                WHERE recipes.id = %(id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        row = results[0]
        recipe = cls(row)
        recipe_creator_info = {
            "id":row["users.id"],
            "first_name":row["first_name"],
            "last_name":row["last_name"],
            "email":row["email"],
            "password":row["password"],
            "created_at":row["created_at"],
            "updated_at":row["updated_at"]
        }
        creator = user.User(recipe_creator_info)
        recipe.creator = creator
        return recipe

    @classmethod
    def update_recipe(cls,data,recipe_id):
        query = """
                UPDATE recipes SET
                name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, under_30 = %(under_30)s, user_id = %(user_id)s
                WHERE id = %(id)s;
                """
        recipe_data = dict(data)
        recipe_data["id"] = recipe_id
        return connectToMySQL(cls.DB).query_db(query,recipe_data)

    @classmethod
    def delete_recipe(cls,recipe_id):
        data = {"id":recipe_id}
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)