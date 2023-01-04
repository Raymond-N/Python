from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import product

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

    @classmethod
    def get_category_products(cls,id):
        data = {"id":id}
        query = """
                SELECT * FROM products
                JOIN categories ON products.category_id = categories.id
                WHERE categories.id = %(id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        print("__GET ALL PRODUCTS__",results)
        products = []
        for the_product in results: 
            new_product = product.Product(the_product)
            category_data = {
                "id" : the_product["categories.id"],
                "name" : the_product["categories.name"],
                "created_at" : the_product["categories.created_at"],
                "updated_at" : the_product["categories.updated_at"]
            }
            product_category = cls(category_data)
            new_product.category = product_category
            products.append(new_product)
        return products