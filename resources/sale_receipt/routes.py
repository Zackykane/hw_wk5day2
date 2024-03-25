from flask import request

from app import app
from db import sale_receipts

@app.route('/')
def land_sale_receipts():
    return {
        "Welcome to our sale reciepts!!!!" : "If your here, you probably need a coffee right about now!"
    }

@app.route('/sale_receipts')
def get_sale_receipts():
    return {
        'sale_receipts' : list(sale_receipts.values())
    }
@app.route('/sale_receipt/<int:id>')
def get_ind_sale_receipt(id):
    if id in sale_receipts:
        return {
            'sale_receipts' : sale_receipts[id]
        }
    return {
        'UH OH, something went wrong' : "invalid sale_receipt id"
    }

@app.route('/sale_receipt', methods=["POST"])
def create_sale_receipt():
    data = request.get_json()
    print(data)
    sale_receipts[data['id']] = data
    return {
        'sale_receipt created successfully': sale_receipts[data['id']]
    }

@app.route('/sale_receipt', methods=["PUT"])
def update_sale_receipt():
    sale_receipt_data = request.get_json()
    if sale_receipt_data['id'] in sale_receipts:
        sale_receipts[sale_receipt_data['id']] = sale_receipt_data
        return {
            'car updated' : sale_receipts[sale_receipt_data['id']]
        }
    return {
        'err' : 'no car found with that id'
    }
    
@app.route('/sale_receipt', methods=["DELETE"])
def delete_sale_receipt():
    sale_receipt_data = request.get_json()
    sale_receipt_id = sale_receipt_data['id']

    if sale_receipt_id not in sale_receipts:
        return { 'message' : "Invalid sale_receipt"}, 400
    
    sale_receipts.pop(sale_receipt_id)
    return {'message': f'sale_receipt: {sale_receipt_id} deleted'}