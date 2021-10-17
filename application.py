from flask import Flask, render_template, session, request, redirect, flash
from flask_mysqldb import MySQL
from flask_session import Session
from tempfile import mkdtemp
from helpers import apology, query_database
from classes import Product, User, Card

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


@app.route('/', methods=["GET", "POST"])
# @login_required
def index():
    global CURRENT_USER
    inventory = []
    records = query_database(mysql, "SELECT product.id, name, price, stock_count FROM catalogue LEFT JOIN product ON catalogue.product_id = product.id ORDER BY product.id;")  
    for record in records:
        inventory.append(Product(record))
    if request.method == 'POST':
        CURRENT_USER.basket.add_product(inventory[int(request.form.get('submit'))-1])
        return redirect("/")
    elif request.method == 'GET':
        return render_template('index.html', title='Products', products=inventory)

@app.route('/login', methods=["GET", "POST"])
def login():
    """Login with username and password"""
    global CURRENT_USER
    # Forget any stored or cached user_ids
    session.clear()

    # If submitting the form
    if request.method == "POST":
        # Ensure username and password fields were completed
        if not request.form.get("username"):
            return apology("must provide username", 403)
        elif not request.form.get("password"):
            return apology("must provide password", 403)
    
        results = query_database(mysql, "SELECT id, username, password FROM customer WHERE username = '" + request.form.get("username") + "';")
    
        # Make sure that one user was returned from the database
        if len(results) != 1:
            return apology("invalid username and/or password", 403)

        CURRENT_USER = User(results[0][0], results[0][1], results[0][2])
        print("Basket = " + str(CURRENT_USER.basket))

        # Make sure the password is correct
        if CURRENT_USER.password != request.form.get("password"):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = CURRENT_USER.id

        # Redirect user to home page
        return redirect("/")

    # User reached by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route('/register')
def register():
    """Register for a new account"""
    return render_template('register.html')

@app.route('/checkout', methods=["GET", "POST"])
def checkout():
    """Checkout with current basket"""
    global CURRENT_USER
    current_total = CURRENT_USER.basket.calculate_total()
    if request.method == "POST":
        print(request.form.get('submit'))
        if request.form.get('submit') == 'shop':
            return redirect("/")
        elif request.form.get('submit') == 'pay':
            return redirect("/payment")
    elif request.method == "GET":    
        return render_template('checkout.html', title='Checkout', products=CURRENT_USER.basket.products, total=current_total)

@app.route('/payment', methods=["GET", "POST"])
def payment():
    """Enter Payment Details"""
    global CURRENT_USER
    current_total = CURRENT_USER.basket.calculate_total()
    if request.method == "GET":
        results = query_database(mysql, "SELECT card.number, sort_code, type, expiry_date, cvv FROM card JOIN customer ON card.number = customer.card_number WHERE customer.id = " + str(CURRENT_USER.id) + ";")
        current_users_card = Card(results[0][0], results[0][1], results[0][2], results[0][3], results[0][4])
        return render_template('payment.html', title='Payment', total=current_total, card=current_users_card)
    elif request.method == "POST":
        if request.form.get('submit') == 'pay':
            print("PAID")
            return redirect("/")
        elif request.form.get('submit') == 'cancel':       
            return redirect("/checkout")
        return redirect("/")
    
@app.route('/logout')
def logout():
  """Log user out"""

  # Clear the current user's details
  session.clear()

  # Redirect user to login form
  return redirect("/login")

  
if __name__ == '__main__':
    app.run(host='0.0.0.0')
