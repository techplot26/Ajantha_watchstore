from flask import Flask, render_template, redirect, url_for, session, request
from models import db, Product, Order, OrderDetail  # Import db from models

app = Flask(__name__)
app.secret_key = "your_secret_key_here"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ajantha.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Initialize db with app

# ----------------- Routes -----------------
@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)
@app.route('/product/<int:product_id>')


def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

@app.route('/basket')
def basket():
    basket = session.get('basket', [])
    products = Product.query.filter(Product.id.in_(basket)).all() if basket else []
    return render_template('basket.html', products=products)

@app.route('/add_to_basket/<int:product_id>')
def add_to_basket(product_id):
    basket = session.get('basket', [])
    if product_id not in basket:
        basket.append(product_id)
    session['basket'] = basket
    return redirect(url_for('basket'))

@app.route('/remove_from_basket/<int:product_id>')
def remove_from_basket(product_id):
    basket = session.get('basket', [])
    if product_id in basket:
        basket.remove(product_id)
    session['basket'] = basket
    return redirect(url_for('basket'))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        session.pop('basket', None)
        return render_template('checkout.html', success=True)
    return render_template('checkout.html', success=False)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)
