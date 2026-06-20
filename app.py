from flask import Flask, render_template, redirect, url_for, request, session
from models import db, Product, Order, OrderDetail
from forms import CheckoutForm
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()
    if Product.query.count() == 0:
        sample_products = [
            Product(name="Ajantha Classic Chrono", description="Elegant chronograph watch with leather strap.", price=199.99, image="images/watch1.jpg", category="Analog"),
            Product(name="Ajantha Slim Minimalist", description="Slim design for a modern look.", price=149.99, image="images/watch2.jpg", category="Analog"),
            Product(name="Ajantha Diamond Luxe", description="Luxury diamond-studded watch.", price=499.99, image="images/watch3.jpg", category="Analog"),
            Product(name="Ajantha Sport Pro", description="Durable sports watch with stopwatch.", price=129.99, image="images/watch4.jpg", category="Digital"),
            Product(name="Ajantha Elegant Silver", description="Silver finish watch perfect for formal occasions.", price=179.99, image="images/watch5.jpg", category="Smart")
        ]
        db.session.add_all(sample_products)
        db.session.commit()

# --- Routes ---

@app.route('/')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)

def get_basket_order():
    order_id = session.get('order_id')
    if order_id:
        order = Order.query.get(order_id)
        if order and not order.completed:
            return order
    order = Order(completed=False)
    db.session.add(order)
    db.session.commit()
    session['order_id'] = order.id
    return order

@app.route('/add_to_basket/<int:product_id>')
def add_to_basket(product_id):
    order = get_basket_order()
    product = Product.query.get_or_404(product_id)
    order_detail = OrderDetail.query.filter_by(order_id=order.id, product_id=product.id).first()
    if order_detail:
        order_detail.quantity += 1
    else:
        order_detail = OrderDetail(order_id=order.id, product_id=product.id, quantity=1)
        db.session.add(order_detail)
    db.session.commit()
    return redirect(url_for('basket'))

@app.route('/basket')
def basket():
    order = get_basket_order()
    return render_template('basket.html', order=order)

@app.route('/remove_item/<int:item_id>')
def remove_item(item_id):
    order_detail = OrderDetail.query.get_or_404(item_id)
    db.session.delete(order_detail)
    db.session.commit()
    return redirect(url_for('basket'))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    order = get_basket_order()
    form = CheckoutForm()
    if form.validate_on_submit():
        order.customer_name = form.customer_name.data
        order.customer_address = form.customer_address.data
        order.completed = True
        db.session.commit()
        session.pop('order_id', None)
        return render_template('checkout.html', order=order, completed=True)
    return render_template('checkout.html', order=order, form=form, completed=False)

if __name__ == '__main__':
    app.run(debug=True)
