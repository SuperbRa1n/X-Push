from flask import Flask, render_template,request,jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/count', methods=['POST'])
def tt_data():
    if request.method == 'POST':
        data = request.get_json() # 获取POST请求中的data参数
        return jsonify({"challenge":data["challenge"]}) 