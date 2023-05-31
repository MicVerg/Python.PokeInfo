import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

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

# Make sure API key is set
# export API_KEY=pk_e0169742106d4b828465d84d24eaff7f
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


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
    # display table with all stocks, number of shares, current price, total value
    user_id = session["user_id"]
    currentShares = db.execute("SELECT * FROM transactions WHERE user_id = ?", user_id)
    # display current cash
    userInfo = db.execute("SELECT * FROM users WHERE id = ?", user_id)
    # display total value (current cash + stocks)
    totalValue = 0
    totalValue2 = 0
    for share in currentShares:
        updatedValue = lookup(share["symbol"])
        totalValue += share["shares"] * updatedValue["price"]
    totalValue2 = totalValue + userInfo[0]["cash"]
    return render_template("index.html", currentShares = currentShares, userInfo = userInfo, totalValue2 = totalValue2, updatedValue = updatedValue)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    # when GET display form to buy stock
    # HTML form should ask for stock symbol and number of shares AND check for valid input(negative number, stock symbol OK?)
    if request.method == "GET":
        return render_template("buy.html")

    elif request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        quote = lookup(symbol)

        if not symbol:
            return apology("Please enter a stock symbol")
        if not quote:
            return apology("Invalid stock symbol")
        if not shares.isdigit():
            return apology("Enter a positive number of shares to buy")
        if int(shares) <= 0:
            return apology("Amount must be minimal 1")

    # add SQL table(s) with CREATE TABLE transactions = user, symbol, amount, price, timestamp

    # when POST buy the stock if user has enough money, if not = apology
    user_id = session["user_id"]
    currentCashQry = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    currentCash = currentCashQry[0]["cash"]
    transactionCost = quote["price"] * int(shares)
    current_timestamp = datetime.now()

    # if yes, run SQL on db to purchase stock
    # update transactions and update cash
    if currentCash >= transactionCost:
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price, timestamp) VALUES (?, ?, ?, ?, ?)", user_id, symbol, shares, quote["price"], current_timestamp)
        newCash = currentCash - transactionCost
        db.execute("UPDATE users SET cash = ? WHERE id = ?", newCash, user_id)
        return redirect("/")
    else:
        return apology("You ain't got no money")



@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # show table with history of transactions for every buy and sell

    #
    return apology("history")


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
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
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
    # when GET, display form to request a stock quote
    if request.method == "GET":
        return render_template("quote.html")
    # when POST, lookup stock symbol by lookup function and display result
    elif request.method == "POST":
        symbol = request.form.get("symbol")

        if not symbol:
            return apology("Please enter a stock symbol")

        quote = lookup(symbol)
        if not quote:
            return apology("Invalid stock symbol")

        return render_template("quoted.html", quote=quote, usd=usd)



@app.route("/register", methods=["GET", "POST"])
def register():
    # when GET, display registration form (make new register.html)
    if request.method == "GET":
        return render_template("register.html")
    # when POST, check for errors and insert new user into users table (any field is empty -> apo, pw & confirm -> apo, username taken -> apo)
    elif request.method == "POST":
        if not request.form.get("username"):
            return apology("Must provide username", 403)

        elif not request.form.get("password"):
            return apology("Must provide password", 403)

        elif not request.form.get("confirmpassword"):
            return apology("Must confirm password", 403)

        elif request.form.get("password") != request.form.get("confirmpassword"):
            return apology("Passwords must match", 403)

        # check if user exists already
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        if rows:
            return apology("Username already taken", 403)

        #complete registration
        # once confirmed, generate_password_hash and add that hash to the database
        # db.execute to add to table
        else:
            hashedpw = generate_password_hash(request.form.get("password"))
            username = request.form.get("username")
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hashedpw)
            rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
            session["user_id"] = rows[0]["id"]
            return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # when GET, display form
    if request.method == "GET":
        return render_template("sell.html")
    # when POST, check for errors (does user have stocks, negative number?)
    elif request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        quote = lookup(symbol)

    # errors
        if not symbol:
            return apology("Please enter a stock symbol")
        if not quote:
            return apology("Invalid stock symbol")
        if not shares.isdigit():
            return apology("Enter a positive number of shares to buy")
        if int(shares) <= 0:
            return apology("Amount must be minimal 1")

    user_id = session["user_id"]
    symbol = request.form.get("symbol")
    shares = request.form.get("shares")
    currentCashQry = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    currentCash = currentCashQry[0]["cash"]
    transactionCost = quote["price"] * int(shares)
    current_timestamp = datetime.now()
    currentSharesQry = db.execute("SELECT SUM(shares) AS total_shares FROM transactions WHERE symbol = ?", symbol)
    currentShares = currentSharesQry[0]["total_shares"]

    if currentShares >= shares:
        shares = -1 * int(shares)
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price, timestamp) VALUES (?, ?, ?, ?, ?)", user_id, symbol, shares, quote["price"], current_timestamp)
        newCash = currentCash + transactionCost
        db.execute("UPDATE users SET cash = ? WHERE id = ?", newCash, user_id)
        return redirect("/")
    else:
        return apology("You don't have that many shares to sell")
