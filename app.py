import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        """Buy shares of stock"""
        # Check if data is valid
        if not request.form.get("stock"):
            return apology("Please enter a stock", 403)
        if not request.form.get("shares"):
            return apology("Please enter share amount", 403)
        shares = int(request.form.get("shares"))
        if shares <= 0:
            return apology("Please enter a positive amount of shares", 403)
        stock_data = lookup(request.form.get("stock"))
        # Check if stock exist
        try:
            stock_data["name"]
        except:
            return apology("The stock does not exist", 403)
        total_price = stock_data["price"] * shares
        user_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]['cash']
        if total_price > user_cash:
            return apology("Not enough funds", 403)
        db.execute("UPDATE users SET cash = ? WHERE id = ?", (user_cash - total_price), session["user_id"])
        db.execute("""INSERT INTO orders (username, type, symbol, shares, total_price, time)
                VALUES (?, ?, ?, ?, ?, datetime('now'))""", 
                session["user_id"], "buy", request.form.get("stock") ,request.form.get("shares"), total_price, )
        return apology("Buying to do, sorryyy", 403)
        
        
        
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
        if request.method == "POST":
            """Get stock quote."""
            if not request.form.get("stock"):
                return apology("must provide stock", 403)
            stock_data = lookup(request.form.get("stock"))
            try:
                stock_data["name"]
                return render_template("quoted.html", name = stock_data["name"], price = stock_data["price"], symbol = stock_data["symbol"] )
            except:
                return apology("Invalid stock", 403)

            




        else:
            return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        if not request.form.get("username"):
            return apology("must provide username", 403)
        if not request.form.get("password"):
            return apology("must provide password", 403)
        if not request.form.get("password_confirm"):
            return apology("must provide password confirm", 403)
        print(request.form.get("username"))
        print(request.form.get("password"))
        print(request.form.get("password_confirm"))
        if request.form.get("password") != request.form.get("password_confirm"):
            return apology("Both passwords must match", 403)
        password_hash = generate_password_hash(request.form.get("password"))
        try:
            db.execute(
                "INSERT INTO users (username, hash) VALUES (?, ?)",request.form.get("username"), password_hash
            )
            return render_template("registered.html", message = request.form.get("username")) 
        except ValueError:
            return apology("Sorry, username already taken", 403)

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")

if __name__ == "__main__":
    app.run(debug=True)