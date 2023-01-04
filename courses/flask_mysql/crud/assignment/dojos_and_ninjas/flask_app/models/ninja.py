from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

class Ninja:
    DB = "dojos_and_ninjas_schema"

    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.dojo_id = data["dojo_id"]
        self.dojo = None

    @classmethod
    def get_all_ninjas(cls):
        query = """
                SELECT * FROM ninjas
                JOIN dojos ON ninjas.dojo_id = dojos.id;
                """
        results = connectToMySQL(cls.DB).query_db(query)
        print("__GET ALL NINJAS__",results)
        ninjas = []
        for ninja in results: 
            new_ninja = cls(ninja)
            dojo_data = {
                "id" : ninja["dojos.id"],
                "name" : ninja["name"],
                "created_at" : ninja["dojos.created_at"],
                "updated_at" : ninja["dojos.updated_at"]
            }
            ninja_dojo = dojo.Dojo(dojo_data)
            new_ninja.dojo = ninja_dojo
            ninjas.append(new_ninja)
        return ninjas

    @classmethod
    def get_ninja_by_id(cls,id):
        data = {"id":id}
        query = """
                SELECT * FROM ninjas
                JOIN dojos ON ninjas.dojo_id = dojos.id
                WHERE ninjas.id = %(id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        print("__GET ONE NINJA__",results)
        ninja = results[0]
        new_ninja = cls(ninja)
        dojo_data = {
            "id" : ninja["dojos.id"],
            "name" : ninja["name"],
            "created_at" : ninja["dojos.created_at"],
            "updated_at" : ninja["dojos.updated_at"]
        }
        ninja_dojo = dojo.Dojo(dojo_data)
        new_ninja.dojo = ninja_dojo
        return new_ninja

    @classmethod
    def create_ninja(cls,data):
        print("__FORM DATA__",data)
        query = "INSERT INTO ninjas (first_name,last_name,age,dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s)"
        results = connectToMySQL(cls.DB).query_db(query,data)
        print("__CREATE NINJA__",results)
        return results

    @classmethod
    def delete_ninja(cls,id):
        data = {"id":id}
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        print("__DELETE PRODUCT__",results)
        return results

    @classmethod
    def update_ninja(cls,data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, dojo_id = %(dojo_id)s WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        print("__UPDATE NINJA__",results)
        return results