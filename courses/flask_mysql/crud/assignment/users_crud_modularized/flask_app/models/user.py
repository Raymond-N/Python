from flask_app.config.mysqlconnection import connectToMySQL

class User:
    DB = "users_schema"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        print("__GET ALL USERS__", results)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def create_user(cls, data):
        print("__FORM DATA__", data)
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        results = connectToMySQL(cls.DB).query_db(query, data)
        print("__CREATE USER__", results)
        return results

    @classmethod
    def get_user_by_id(cls,id):
        data = {"id":id}
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        print("__GET ONE USER__",results)
        return cls(results[0])

    @classmethod
    def delete_user(cls,id):
        data = {"id":id}
        query = "DELETE FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        print("__DELETE PRODUCT__",results)
        return results

    @classmethod
    def update_user(cls,data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        print("__UPDATE USER__",results)
        return results
