from flask_app.config.mysqlconnection import connectToMySQL

class Product:
    DB = "products-demo"

    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.price = data["price"]
        self.category_id = data["category_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all_products(cls):
        query = "SELECT * FROM products;"
        results = connectToMySQL(cls.DB).query_db(query)
        print("__GET ALL PRODUCTS__",results)
        products = []
        for product in results:
            products.append(cls(product))
        return products

    @classmethod
    def get_product_by_id(cls,id):
        data = {"id":id}
        query = "SELECT * FROM products WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        print("__GET ONE PRODUCT__",results)
        return cls(results[0])

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