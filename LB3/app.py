from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
import json

# auth
app = Flask(__name__)
auth = HTTPBasicAuth()

# get users from users.json 
with open('users.json', 'r') as f:
    users = json.load(f)

# auth check
@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username
    return None

# catalog load
def load_catalog():
    with open('catalog.json', 'r') as f:
        return json.load(f)

# save catalog data
def save_catalog(data):
    with open('catalog.json', 'w') as f:
        json.dump(data, f, indent=4)

# main
@app.route('/')
def home():
    return jsonify({"message": "main page, you`re welcome!"})

# route
@app.route('/items', methods=['GET', 'POST'])
@auth.login_required
def items():
    catalog = load_catalog()
    
    if request.method == 'GET':
        return jsonify(catalog)
    
    if request.method == 'POST':
        new_item = request.json
        catalog.append(new_item)
        save_catalog(catalog)
        return jsonify({"message": "Товар добавлен!", "item": new_item}), 201

# id stuff
@app.route('/items/<int:item_id>', methods=['GET', 'PUT', 'DELETE'])
@auth.login_required
def item_by_id(item_id):
    catalog = load_catalog()
    item = next((item for item in catalog if item['id'] == item_id), None)
    
    if not item:
        return jsonify({"error": "there is no such good"}), 404
    
    if request.method == 'GET':
        return jsonify(item)
    
    if request.method == 'PUT':
        data = request.json
        item.update(data)
        save_catalog(catalog)
        return jsonify({"message": "updated", "item": item})
    
    if request.method == 'DELETE':
        catalog = [item for item in catalog if item['id'] != item_id]
        save_catalog(catalog)
        return jsonify({"message": "deleted"})

if __name__ == '__main__':
    app.run(debug=True)
