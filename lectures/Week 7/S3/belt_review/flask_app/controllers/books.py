from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models import user,book

@app.route("/new/book")
def add_book():
    if "user_id" not in session:
        return redirect("/")
    current_user = user.User.get_by_id(session["user_id"])
    return render_template("add-book.html",user=current_user)

@app.route("/add-book",methods=["POST"])
def create_book():
    if "user_id" not in session:
        return redirect("/")
    if book.Book.validate_book(request.form):
        book.Book.create_book(request.form)
        return redirect("/dashboard")
    return redirect("/new/book")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/")
    current_user = user.User.get_by_id(session["user_id"])
    all_books = book.Book.get_all_books()
    return render_template("dashboard.html",user=current_user,books=all_books)

@app.route("/show/<int:id>")
def get_book(id):
    if "user_id" not in session:
        return redirect("/")
    current_user = user.User.get_by_id(session["user_id"])
    current_book = book.Book.get_book(id)
    is_fav = book.Book.is_favorite({"user_id":current_user.id,"book_id":current_book.id})
    return render_template("book-details.html",user=current_user,book=current_book,is_fav=is_fav)

@app.route("/edit/<int:id>")
def update_book(id):
    if "user_id" not in session:
        return redirect("/")
    
    current_user = user.User.get_by_id(session["user_id"])
    current_book = book.Book.get_book(id)
    return render_template("edit-book.html",user=current_user,book=current_book)

@app.route("/edit-book/<int:id>",methods=["POST"])
def edit_book(id):
    if "user_id" not in session:
        return redirect("/")
    if book.Book.validate_book(request.form):
        book.Book.update_book(request.form,id)
        return redirect(f"/show/{id}")
    return redirect(f"/edit/{id}")

@app.route("/user/account")
def my_books():
    if "user_id" not in session:
        return redirect("/")
    current_user = user.User.get_by_id(session["user_id"])
    all_books = book.Book.get_user_books(current_user.id)
    return render_template("my-books.html",books=all_books,user=current_user)

@app.route("/books/delete/<int:id>")
def delete_book(id):
    if "user_id" not in session:
        return redirect("/")
    book.Book.delete_book(id)
    return redirect("/user/account")

@app.route("/books/<int:book_id>/<int:user_id>/add-to-fav")
def add_to_fav(book_id,user_id):
    if "user_id" not in session:
        return redirect("/")
    book.Book.add_to_favorite({"user_id":user_id,"book_id":book_id})
    return redirect(f"/show/{book_id}")

@app.route("/books/<int:book_id>/<int:user_id>/remove-from-fav")
def remove_from_fav(book_id,user_id):
    if "user_id" not in session:
        return redirect("/")
    data = {"user_id":user_id,"book_id":book_id}
    book.Book.remove_from_favorite(data)
    return redirect(f"/show/{book_id}")