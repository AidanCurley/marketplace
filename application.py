from flask import Flask, render_template, session, request, redirect, flash
from flask_mysqldb import MySQL
from flask_session import Session
from tempfile import mkdtemp

from helpers import apology, create_inventory, get_users_inventory, query_database, update_database
from classes import Product, User, Card, OnlinePayment, Voucher
from errors import *
import constants

from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'codio'
app.config['MYSQL_DB'] = 'marketplace'
# Configure session to use filesystem instead of cookies
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
mysql = MySQL(app)


@app.route('/login', methods=["GET", "POST"])
def login():
    """Login with username and password"""
    global CURRENT_USER
    # Forget any stored or cached user_ids
    session.clear()

    if request.method == "GET": # User reached by clicking a link or via redirect)
        return render_template("login.html")
    elif request.method == "POST":  # User clicked a button, submitting the form
        username_on_form = request.form.get("username")
        password_on_form = request.form.get("password")
        # Ensure username and password fields were completed
        if not username_on_form:
            return apology("must provide username", 403)
        elif not password_on_form:
            return apology("must provide password", 403)

        # Check if current user is a customer
        results = query_database(mysql, f"SELECT id, username, password, f_name FROM customer WHERE username = '{username_on_form}' and password = '{password_on_form}';")
        if len(results) == 1:
            create_and_welcome_customer(results)
            # Redirect customer to shopping page
            return redirect("/")
        # If not a customer, check if current_user is a seller
        else:
            results = query_database(mysql, f"SELECT id, username, password, f_name, storefront FROM seller WHERE username = '{username_on_form}' and password = '{password_on_form}';")
            if len(results) == 1:
                create_and_welcome_seller(results)
                # Redirect seller to seller dashboard
                return redirect("/sellerdashboard")
            else: # If neither customer nor seller, return apology
                return apology(f"{constants.INVALID_LOGIN}", 403)

@app.route('/register')
def register():
    """Register for a new account"""
    return render_template('register.html')


@app.route('/', methods=["GET", "POST"])
def products():
    """Landing page for customer with complete list of products for sale on website (from all sellers)"""
    global CURRENT_USER
    if request.method == 'GET': # User reached by clicking a link or via redirect)
        # Get list of all products across all sellers
        inventory = create_inventory(mysql)
        return render_template('index.html', title='Products', products=inventory)
    elif request.method == 'POST':  # User clicks a button, submitting the form
        # Get list of all products across all sellers
        inventory = create_inventory(mysql)
        button_pressed = request.form.get('submit')
        if button_pressed == 'checkout':
            return redirect("/checkout")
        else: # One of the "buy" buttons has been clicked
            #Add product to basket and notify customer
            product_selected = [product for product in inventory if product.id == int(button_pressed)][0]
            CURRENT_USER.basket.add_product(product_selected)
            flash(f"{ product_selected } added to your basket. Your basket now contains {len(CURRENT_USER.basket.products)} items.", 'success')
            return redirect("/")


@app.route('/checkout', methods=["GET", "POST"])
def checkout():
    """Checkout with current basket"""
    global CURRENT_USER
    current_total = CURRENT_USER.basket.calculate_total()

    if request.method == "GET": # User reached by clicking a link or via redirect)
        return render_template('checkout.html', title='Checkout', products=CURRENT_USER.basket.products, total=current_total)
    elif request.method == "POST":  # User clicks a button, submitting the form
        button_pressed = request.form.get('submit')
        if button_pressed == 'empty':
            CURRENT_USER.basket.empty_basket()
            flash(f"Your basket has been emptied.", 'success')
            return redirect("/")
        if button_pressed == 'shop':
            return redirect("/")
        elif button_pressed == 'checkout':
            return redirect("/payment")



@app.route('/payment', methods=["GET", "POST"])
def payment():
    """Enter Payment Details"""
    global CURRENT_USER

    if request.method == "GET": # User reached by clicking a link or via redirect)
        current_total = CURRENT_USER.basket.calculate_total()
        return render_template('payment.html', title='Payment', total=current_total, card=CURRENT_USER.payment_details.card, online_payment=CURRENT_USER.payment_details.online_payment)
    elif request.method == "POST":  # User clicks a button, submitting the form
        current_total = CURRENT_USER.basket.calculate_total()
        button_pressed = request.form.get('submit')
        if button_pressed == 'cancel':
            return redirect("/checkout")
        elif button_pressed == 'pay':
            type_of_payment = request.form.getlist('options')
            # There are three types of payment possible
            try:
                if type_of_payment == ['card']:
                    # Get card details from webpage, set success message
                    payment_method = Card(request.form.get('card_number'), request.form.get('sort_code'), request.form.get('card_type'), request.form.get('expiry_date'), request.form.get('cvv'))
                    message = f"{constants.SUCCESSFUL_PAYMENT_MESSAGE} Your card ending in ***{payment_method.card_number[-4:]} has been charged £{current_total}."
                elif type_of_payment == ['online']:
                    # Get online payment details from webpage, check they exist in db
                    online_payment_details_on_form = OnlinePayment(request.form.get('service_name'), request.form.get('service_number'))
                    results = query_database(mysql, f"SELECT name, number, balance FROM onlinepayment WHERE name = '{online_payment_details_on_form.service_name}' AND number = '{online_payment_details_on_form.service_number}';")
                    # If not found in the db, notify user and return to payment details entry
                    if len(results) == 0:
                        flash(f"{constants.NON_EXISTENT_DETAILS_MESSAGE}", 'error')
                        return redirect("/payment")
                    # Process payment
                    payment_method = OnlinePayment(results[0][0], results[0][1], results[0][2])
                    payment_method.process_payment(current_total)
                    # Write new balance to the database and set success message
                    update_database(mysql, f"UPDATE onlinepayment SET balance='{payment_method.balance}' WHERE name = '{payment_method.service_name}' AND number = '{payment_method.service_number}';")
                    message = f"{constants.SUCCESSFUL_PAYMENT_MESSAGE} Your {payment_method.service_name} account has been charged £{current_total}."
                elif type_of_payment == ['voucher']:
                    # Get voucher details from webpage, check they exist in db
                    voucher_details_on_form = Voucher(request.form.get('voucher_id'))
                    results = query_database(mysql, f"SELECT id, expiry_date, amount FROM voucher WHERE id = '{voucher_details_on_form.voucher_id}';")
                    # If not found in the db, notify user and return to payment details entry
                    if len(results) == 0:
                        flash(f"{constants.NON_EXISTENT_DETAILS_MESSAGE}", 'error')
                        return redirect("/payment")
                    # Process payment
                    payment_method = Voucher(results[0][0], results[0][1], results[0][2])
                    payment_method.process_payment(current_total)
                    # Set success message
                    message = f"{constants.SUCCESSFUL_PAYMENT_MESSAGE} Your voucher {payment_method.voucher_id} cannot be used again."
                # After payment method has been verified, create a transaction, write it to the db, and empty the user's basket
                transaction = CURRENT_USER.basket.create_transaction(payment_method)
                update_database(mysql, f"INSERT INTO transaction (date, customer_id, amount, payment_details) VALUES ('{transaction.date}', {int(CURRENT_USER.id)}, {current_total}, '{str(payment_method)}');")
                CURRENT_USER.basket.empty_basket()
                # Notify user
                flash(f"{message}", 'success')
                return redirect("/")
            except (PaymentError, ExpiryError, ValueError) as e:
                flash(f"{constants.PAYMENT_DECLINED}: {e}", 'error')
                return redirect("/payment")
            except DatabaseError as e:
                return apology(f"{e}", 500)
        return redirect("/")


@app.route('/sellerdashboard', methods=["GET", "POST"])
def sellerdashboard():
    """Landing page for seller with list of current products"""
    global CURRENT_USER
    if request.method == 'GET':   # User reached by clicking a link or via redirect)
        return render_template('sellerdashboard.html', title='Dashboard', products=CURRENT_USER.catalogue.products)
    elif request.method == 'POST':   # User clicks a button, submitting the form
        # Find which button was pressed and pass that products details to the next page
        button_pressed = int(request.form.get('submit'))
        product_selected = [product for product in CURRENT_USER.catalogue.products if product.id == button_pressed][0]
        return render_template('product.html', title='Edit Product', product=product_selected, readonly='readonly')


@app.route('/storefront', methods=["GET", "POST"])
def storefront():
    """Page for seller to edit their storefront"""
    global CURRENT_USER
    if request.method == 'GET':   # User reached by clicking a link or via redirect)
        return render_template('storefront.html', title='Dashboard', storefront=CURRENT_USER.storefront)
    elif request.method == 'POST':   # User clicks a button, submitting the form
        button_pressed = request.form.get('submit')
        if button_pressed == 'cancel':
            return redirect("/sellerdashboard")
        elif button_pressed == 'save':
            try:
                # Get details from the form
                new_storefront = request.form.get('storefront')
                # Update storefront and write to database
                CURRENT_USER.storefront = new_storefront
                update_database(mysql, f"UPDATE seller SET storefront='{new_storefront}' WHERE id={int(CURRENT_USER.id)};")
                # Notify user
                flash(f"{constants.UPDATED_STOREFRONT_MESSAGE}", 'success')
                return redirect("/sellerdashboard")
            except TypeError as e:
                flash(f"{e}", 'error')
                return redirect("/storefront")
            except DatabaseError as e:
                return apology(f"{e}", 500)


@app.route('/product', methods=["GET", "POST"])
def product():
    """Page for seller to edit price of existing product in their catalogue"""
    global CURRENT_USER
    if request.method == 'GET':   # User reached by clicking a link or via redirect)
        return redirect("/product")
    elif request.method == 'POST':   # User clicks a button, submitting the form
        button_pressed = request.form.get('submit')
        if button_pressed == 'cancel':
            return redirect("/sellerdashboard")
        elif button_pressed == 'save':
            try:
                # Get details from the form
                product_id_on_form = int(request.form.get('id'))
                new_price = float(request.form.get('price'))
                product_being_edited = [product for product in CURRENT_USER.catalogue.products if product.id == product_id_on_form][0]
                # Update price and write to database
                product_being_edited.price = new_price
                update_database(mysql, f"UPDATE catalogue SET price={new_price} WHERE seller_id={int(CURRENT_USER.id)} AND product_id={product_id_on_form};")
                # Notify user
                flash(f"{constants.UPDATED_CATALOGUE_MESSAGE}", 'success')
                return redirect("/sellerdashboard")
            except DatabaseError as e:
                return apology(f"{e}", 500)
        return redirect("/sellerdashboard")


@app.route('/newproduct', methods=["GET", "POST"])
def new_product():
    """Page for seller to add a new product to their catalogue"""
    global CURRENT_USER
    if request.method == 'GET':   # User reached by clicking a link or via redirect)
        return render_template('newproduct.html', title='Add New Product')
    elif request.method == 'POST':   # User clicks a button, submitting the form
        button_pressed = request.form.get('submit')
        if button_pressed == 'cancel':
            return redirect("/sellerdashboard")
        elif button_pressed == 'save':
            try:
                # Get details from the form
                new_name = request.form.get('name')
                new_price = float(request.form.get('price'))
                stock_count = int(request.form.get('stock_count'))
                # Create new product id and add product to catalogue
                new_id = query_database(mysql, f"SELECT MAX(id) from product;")[0][0] + 1
                CURRENT_USER.catalogue.add_product(Product([new_id, new_name, new_price, stock_count]))
                # Update product and catalogue tables in the db
                update_database(mysql, f"INSERT INTO product (id, name, stock_count) VALUES ({new_id}, '{new_name}', {stock_count});")
                update_database(mysql, f"INSERT INTO catalogue (product_id, seller_id, price) VALUES ({new_id}, {int(CURRENT_USER.id)}, {new_price});")
                # Notify user
                flash(f"{constants.UPDATED_CATALOGUE_MESSAGE}", 'success')
                return redirect("/sellerdashboard")
            except DatabaseError as e:
                return apology(f"{e}", 500)
        return redirect("/sellerdashboard")


@app.route('/logout')
def logout():
    """Log user out"""
    global CURRENT_USER

    # Clear the current user's details
    session.clear()
    # Redirect user to login form
    return redirect("/login")


# Common methods
def create_and_welcome_customer(details):
    """Create current_user object from the details passed in.
    Flashe welcome message to the user."""
    global CURRENT_USER
    # Create current_user object
    CURRENT_USER = User(details[0][0], details[0][1], details[0][2], details[0][3])
    # Get the user's payment details from the database
    results = query_database(mysql, f"SELECT number, sort_code, type, expiry_date, cvv FROM card JOIN customer ON card.customer_number = customer.id WHERE customer.id = {str(CURRENT_USER.id)};")
    CURRENT_USER.payment_details.card = Card(results[0][0], results[0][1], results[0][2], results[0][3], results[0][4])
    results = query_database(mysql, f"SELECT name, number, balance FROM onlinepayment JOIN customer ON onlinepayment.customer_number = customer.id WHERE customer.id = {str(CURRENT_USER.id)};")
    CURRENT_USER.payment_details.online_payment = OnlinePayment(results[0][0], results[0][1], results[0][2])
    # Remember which user has logged in
    session["user_id"] = CURRENT_USER.id
    flash(f"Welcome {CURRENT_USER.name}", 'message')

def create_and_welcome_seller(details):
    """Create current_user object from the details passed in.
    Flash welcome message to the user."""
    global CURRENT_USER
    # Create current_user object
    CURRENT_USER = User(details[0][0], details[0][1], details[0][2], details[0][3])
    CURRENT_USER.storefront = details[0][4]
    CURRENT_USER.catalogue.products = get_users_inventory(mysql, CURRENT_USER.id)
    # Remember which user has logged in
    session["user_id"] = CURRENT_USER.id
    flash(f"Welcome {CURRENT_USER.name}", 'message')


def errorhandler(e):
    """Handle errors"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # Listen for errors
    for code in default_exceptions:
        app.errorhandler(code)(errorhandler)