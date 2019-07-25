"""Routes exposes public facing end points to an end user."""


from app import app
from flask import jsonify, request
from library_example import lib_example_call

@app.route('/order', methods=['POST'])
def order():
    msg = lib_example_call()
    return jsonify({'message': 'project_b: {}'.format(msg)})

@app.route('/order', methods=['GET'])
def all_orders():
    msg = lib_example_call()
    return jsonify({'message': 'project_b: {}'.format(msg)})
