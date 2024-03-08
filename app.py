from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure, random value

# Sample tea data (you would typically use a database)
teas = [
    {"id": 1, "name": "Green Tea", "price": 10},
    {"id": 2, "name": "Black Tea", "price": 12},
    {"id": 3, "name": "Herbal Tea", "price": 8},
]

cart = []

@app.route('/')
def index():
    return render_template('index.html', teas=teas)

@app.route('/tea/<int:tea_id>')
def tea_detail(tea_id):
    tea = next((t for t in teas if t["id"] == tea_id), None)
    if tea:
        return render_template('tea_detail.html', tea=tea)
    else:
        return "Tea not found", 404

@app.route('/add_to_cart/<int:tea_id>', methods=['POST'])
def add_to_cart(tea_id):
    tea = next((t for t in teas if t["id"] == tea_id), None)
    if tea:
        cart.append(tea)
        flash(f"{tea['name']} added to your cart!", 'success')
    else:
        flash("Tea not found", 'danger')
    return redirect(url_for('index'))

@app.route('/cart')
def view_cart():
    return render_template('cart.html', cart=cart)

if __name__ == '__main__':
    app.run(debug=True)
