from mysqlconnection import connectToMySQL

class Category:
    DB = "products-demo"

    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all_categories(cls):
        query = "SELECT * FROM categories;"
        results = connectToMySQL(cls.DB).query_db(query)
        print("__GET ALL CATEGORIES__",results)
        categories = []
        for category in results:
            categories.append(cls(category))
        return categories

    @classmethod
    def create_category(cls,data):
        print("__FORM DATA__",data)
        query = "INSERT INTO categories (name) VALUES (%(name)s)"
        results = connectToMySQL(cls.DB).query_db(query,data)
        print("__CREATE CATEGORY__",results)
        return results