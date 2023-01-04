from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from flask_app.models import user

class Book:
    DB = "belt_review_many_to_many_demo"

    def __init__(self,data):
        self.id = data["id"]
        self.title = data["title"]
        self.author = data["author"]
        self.publisher = data["publisher"]
        self.publish_date = data["publish_date"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.creator = None
        self.fav_users = []

    @staticmethod
    def validate_book(book):
        is_valid = True
        if not book["title"] or len(book["title"]) < 4:
            flash("title must be at least 4 characters.")
            is_valid = False
        if not book["author"] or len(book["author"]) < 5:
            flash("author must be at least 5 characters.")
            is_valid = False
        if not book["publisher"] or len(book["publisher"]) > 20:
            flash("publisher must be at most 20 characters.")
            is_valid = False
        return is_valid

    @classmethod
    def add_to_favorite(cls,data):
        query = """
                INSERT INTO favorites (user_id,book_id)
                VALUES (%(user_id)s,%(book_id)s);
                """
        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def remove_from_favorite(cls,data):
        query = """
                DELETE FROM favorites WHERE book_id = %(book_id)s AND user_id = %(user_id)s;
                """
        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def is_favorite(cls,data):
        query = """
                SELECT * FROM favorites WHERE book_id = %(book_id)s AND user_id = %(user_id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        if len(results) == 0:
            return False
        return True

    @classmethod
    def get_all_books(cls):
        query = """
                SELECT * FROM books JOIN users ON books.user_id = users.id
                ORDER BY books.created_at
                """
        results = connectToMySQL(cls.DB).query_db(query)
        books = []

        for row in results:
            book = cls(row)
            book_creator_info = {
                "id" : row["users.id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "email" : row["email"],
                "password" : row["password"],
                "created_at" : row["users.created_at"],
                "updated_at" : row["users.updated_at"]
            }
            creator = user.User(book_creator_info)
            book.creator = creator
            books.append(book)
        return books

    @classmethod
    def get_user_books(cls,user_id):
        data = {"user_id":user_id}
        query = """
                SELECT * FROM books
                WHERE user_id = %(user_id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        books = []
        for row in results:
            book = cls(row)
            books.append(book)
        return books

    @classmethod
    def get_book(cls,book_id):
        data = {"id" : book_id}
        query = """
                SELECT * FROM books 
                LEFT JOIN users AS creator ON creator.id = books.user_id
                LEFT JOIN favorites ON books.id = favorites.book_id
                LEFT JOIN users AS fav_user ON fav_user.id = favorites.user_id
                WHERE books.id = %(id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        book = cls(results[0])
        book_data = results[0]
        book_creator_info = {
            "id" : book_data["creator.id"],
            "first_name" : book_data["first_name"],
            "last_name" : book_data["last_name"],
            "email" : book_data["email"],
            "password" : book_data["password"],
            "created_at" : book_data["creator.created_at"],
            "updated_at" : book_data["creator.updated_at"]
        }
        creator = user.User(book_creator_info)
        book.creator = creator
        for row in results:
            if not row["fav_user.id"]:
                break
            user_fav_info = {
                "id" : row["fav_user.id"],
                "first_name" : row["fav_user.first_name"],
                "last_name" : row["fav_user.last_name"],
                "email" : row["fav_user.email"],
                "password" : row["fav_user.password"],
                "created_at" : row["fav_user.created_at"],
                "updated_at" : row["fav_user.updated_at"]
            }
            book.fav_users.append(user.User(user_fav_info))
        return book

    @classmethod
    def update_book(cls,data,book_id):
        query = """
                UPDATE books SET
                title = %(title)s, author = %(author)s, publisher = %(publisher)s, publish_date = %(publish_date)s, user_id = %(user_id)s
                WHERE id = %(id)s;
                """
        book_data = dict(data)
        book_data["id"] = book_id
        return connectToMySQL(cls.DB).query_db(query,book_data)

    @classmethod
    def delete_book(cls,book_id):
        data = {"id":book_id}
        query = "DELETE FROM books WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)