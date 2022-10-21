import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/api/customers')
def handle_get_customers():
    return json.dumps([]), 200


@app.route('/api/customers/<int:customer_id>')
def handle_get_customer_by_id(customer_id):
    # this handler method is not ready yet
    return json.dumps({'id': customer_id}), 200


@app.route('/')
def index():
    # the html files are located in "templates" folder
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')