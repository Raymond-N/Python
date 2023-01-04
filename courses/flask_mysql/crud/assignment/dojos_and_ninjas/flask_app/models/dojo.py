from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    DB = "dojos_and_ninjas_schema"

    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.DB).query_db(query)
        print("__GET ALL DOJOS__",results)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def create_dojo(cls,data):
        print("__FORM DATA__",data)
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"
        results = connectToMySQL(cls.DB).query_db(query,data)
        print("__CREATE DOJO__",results)
        return results

    @classmethod
    def get_dojo_ninjas(cls,id):
        data = {"id":id}
        query = """
                SELECT * FROM ninjas
                JOIN dojos ON ninjas.dojo_id = dojos.id
                WHERE dojos.id = %(id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        print("__GET ALL NINJAS__",results)
        ninjas = []
        for the_ninja in results:
            new_ninja = ninja.Ninja(the_ninja)
            dojo_data = {
                "id" : the_ninja["dojos.id"],
                "name" : the_ninja["name"],
                "created_at" : the_ninja["dojos.created_at"],
                "updated_at" : the_ninja["dojos.updated_at"]
            }
            ninja_dojo = cls(dojo_data)
            new_ninja.dojo = ninja_dojo
            ninjas.append(new_ninja)
        return ninjas