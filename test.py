import json
from flask import Flask

app = Flask(__name__)


@app.route('/api/customers')
def handle_get_customers():
    return json.dumps([]), 200


@app.route('/api/customers/<int:customer_id>')
def handle_get_customer_id():
    return None, 200

@app.route('/')
def index():
    return render_template('index.html')
