from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample products
products = [
    {"id": 1, "name": "Rose Bouquet", "price": 999},
    {"id": 2, "name": "Tulip Bouquet", "price": 1299},
    {"id": 3, "name": "Lily Bouquet", "price": 899},
    {"id": 4, "name": "Mixed Flowers", "price": 1499}
]

cart = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def get_products():
    return jsonify(products)

@app.route('/add-to-cart/<int:id>')
def add_to_cart(id):
    for p in products:
        if p["id"] == id:
            cart.append(p)
            break
    return jsonify({"message": "Added to cart"})

@app.route('/cart')
def get_cart():
    return jsonify(cart)

@app.route('/remove-from-cart/<int:index>')
def remove_from_cart(index):
    if index < len(cart):
        cart.pop(index)
    return jsonify({"message": "Removed"})

if __name__ == '__main__':
    app.run(debug=True)