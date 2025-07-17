from flask import Flask, render_template, request, redirect, url_for, session
import random
import time

app = Flask(__name__)
app.secret_key = 'your_super_secret_key_here' # session management

# In-memory storage for products (for demonstration purposes in Sprint 1)
_tracked_products_data = [
    {'id': 1, 'title': 'Mentos Pure Fresh Sugar-Free Chewing Gum', 'currentPrice': '$11.98', 'targetPrice': '$10.00', 'url': 'https://www.amazon.com/Mentos-Pure-Fresh-Sugar-Free-Chewing/dp/B001EO5Q3Q'},
    {'id': 2, 'title': 'History Year by Year: The History of the World', 'currentPrice': '$9.93', 'targetPrice': '$8.00', 'url': 'https://www.amazon.com/History-Year-World-DK/dp/1465408316'},
    {'id': 3, 'title': 'Gatorade Thirst Quencher Powder', 'currentPrice': '$15.98', 'targetPrice': '$14.98', 'url': 'https://www.amazon.com/Gatorade-Thirst-Quencher-Powder-Glacier/dp/B0776HZ26P'},
]

# --- Routes for each page ---

@app.route('/')
def welcome():
    """Renders the Welcome page."""
    return render_template('welcome.html')

@app.route('/login', methods=['POST'])
def login():
    """Handles login (simulated) and redirects to home."""
    # TODO: validate credentials here
    # For Sprint 1, just redirect to home
    return redirect(url_for('home'))

@app.route('/home')
def home():
    """Renders the Home page."""
    return render_template('home.html')

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    """
    Renders the Add New Product page and handles product submission.
    GET: Displays the form.
    POST: Processes the form data and adds a new product.
    """
    if request.method == 'POST':
        product_url = request.form['product_url']
        target_price = request.form['target_price']

        if product_url and target_price:
            # Simulate adding product with placeholder values for title and currentPrice
            new_product = {
                'id': int(time.time() * 1000), # Unique ID
                'title': f'Product from {product_url[:20]}...',
                'currentPrice': f'${random.uniform(10, 60):.2f}',
                'targetPrice': f'${float(target_price):.2f}',
                'url': product_url,
            }
            _tracked_products_data.append(new_product)
            return redirect(url_for('tracked_products'))
        else:
            return render_template('add_product.html', error="Please enter both product URL and target price.")
    return render_template('add_product.html')

@app.route('/tracked_products')
def tracked_products():
    """Renders the Tracked Products page with the list of products."""
    return render_template('tracked_products.html', products=_tracked_products_data)

@app.route('/delete_product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    """Deletes a product from the tracked list."""
    global _tracked_products_data # Declare intent to modify the global variable
    # Find and remove the product
    _tracked_products_data = [p for p in _tracked_products_data if p['id'] != product_id]
    return redirect(url_for('tracked_products'))

if __name__ == '__main__':
    app.run(debug=True)
