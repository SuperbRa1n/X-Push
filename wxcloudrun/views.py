from flask import Flask, render_template,request,jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world!"

@app.route('/IoT_H2')
def hello_H2():
    return "Hello,IoT_H2"

@app.route('/post', methods=['GET','POST'])
def post_example():
    if request.method == 'POST':
        data = request.get_json() # 获取POST请求中的data参数
        return jsonify({"challenge":data["challenge"]})