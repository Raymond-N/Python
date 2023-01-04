from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import category

class Product:
    DB = "products-demo"

    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.price = data["price"]
        self.category_id = data["category_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.category = None

    @classmethod
    def get_all_products(cls):
        query = """
                SELECT * FROM products
                JOIN categories ON products.category_id = categories.id;
                """
        results = connectToMySQL(cls.DB).query_db(query)
        print("__GET ALL PRODUCTS__",results)
        products = []
        for product in results: 
            new_product = cls(product)
            category_data = {
                "id" : product["categories.id"],
                "name" : product["categories.name"],
                "created_at" : product["categories.created_at"],
                "updated_at" : product["categories.updated_at"]
            }
            product_category = category.Category(category_data)
            new_product.category = product_category
            products.append(new_product)
        return products

    @classmethod
    def get_product_by_id(cls,id):
        data = {"id":id}
        query = """
                SELECT * FROM products
                JOIN categories ON products.category_id = categories.id
                WHERE products.id = %(id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        print("__GET ALL PRODUCTS__",results)
        product = results[0]
        new_product = cls(product)
        category_data = {
            "id" : product["categories.id"],
            "name" : product["categories.name"],
            "created_at" : product["categories.created_at"],
            "updated_at" : product["categories.updated_at"]
        }
        product_category = category.Category(category_data)
        new_product.category = product_category
        return new_product

    @classmethod
    def create_product(cls,data):
        print("__FORM DATA__",data)
        query = "INSERT INTO products (name,price,category_id) VALUES (%(name)s,%(price)s,%(category_id)s)"
        results = connectToMySQL(cls.DB).query_db(query,data)
        print("__CREATE PRODUCT__",results)
        return results

    @classmethod
    def delete_product(cls,id):
        data = {"id":id}
        query = "DELETE FROM products WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        print("__DELETE PRODUCT__", results)
        return results

    @classmethod
    def update_product(cls,data):
        query = "UPDATE products SET name = %(name)s, price = %(price)s, category_id = %(category_id)s WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        print("__UPDATE PRODUCT__",results)
        return results