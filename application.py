from flask import Flask, render_template, session, request, redirect, flash
from flask_mysqldb import MySQL
from flask_session import Session
from tempfile import mkdtemp
from helpers import apology

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'codio'
app.config['MYSQL_DB'] = 'marketplace'
# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
mysql = MySQL(app)

@app.route('/')
# @login_required
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT name, price, stock_count FROM product JOIN catalogue ON product.id = catalogue.product_id;")
    products = cursor.fetchall()
    cursor.close()
    return render_template('index.html', title='Products', products=products)

@app.route('/login', methods=["GET", "POST"])
def login():
  """Login with username and password"""
  # Forget any stored or cached user_ids
  session.clear()

  # If submitting the form
  if request.method == "POST":
    # Ensure username and password fields were completed
    if not request.form.get("username"):
      return apology("must provide username", 403)
    elif not request.form.get("password"):
      return apology("must provide password", 403)

    # Open connection to db and query for user's record
    cursor = mysql.connection.cursor()
    username = request.form.get("username")
    cursor.execute("SELECT * FROM customer WHERE username = '" + username + "';")
    users = cursor.fetchall()
    cursor.close()
    # Ensure username exists and password is correct
    if len(users) != 1 or users[0][2] != request.form.get("password"):
      return apology("invalid username and/or password", 403)

    # Remember which user has logged in
    session["user_id"] = users[0][0]

    # Redirect user to home page
    return redirect("/")

  # User reached by clicking a link or via redirect)
  else:
    return render_template("login.html")


@app.route('/register')
def register():
  """Register for a new account"""
  return render_template('register.html')

@app.route('/checkout')
def checkout():
  """Checkout with current basket"""
  return render_template('checkout.html')


@app.route('/logout')
def logout():
  """Log user out"""

  # Clear the current user's details
  session.clear()

  # Redirect user to login form
  return redirect("/login")

  
if __name__ == '__main__':
    app.run(host='0.0.0.0')
