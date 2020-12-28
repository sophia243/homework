from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def homework():
    return render_template('index.html')

@app.route('/order', methods=['post'])
def save_order():
    name_receive = request.form['name_give']
    color_receive = request.form['color_give']
    count_receive = request.form['count_give']
    add_receive = request.form['add_give']
    phone_receive = request.form['phone_give']

    doc = {
        'name': name_receive,
        'color': color_receive,
        'count': count_receive,
        'add': add_receive,
        'phone': phone_receive
    }

    db.homework.insert_one(doc)

    return jsonify({'result': 'success', 'msg':'주문되었습니다.'})


@app.route('/order', methods=['GET'])
def view_order():
    order = list(db.orders.find({}, {'_id':False}))
    return jsonify({'result': 'success', 'orders': order})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)