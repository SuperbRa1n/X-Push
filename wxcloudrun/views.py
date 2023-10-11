from flask import Flask, render_template,request,jsonify
import json

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        data = request.get_json() # 获取POST请求中的data参数
        return jsonify({"challenge":data["challenge"]}) 