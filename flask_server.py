#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, render_template
from flask_cors import CORS

from trans_sig import trans_sig

app = Flask(__name__,template_folder='/home/pi/I2C0x52-IR/remocon/dist')
CORS(app,supports_credentials=True)

@app.route("/api/trans-sig", methods=["GET"])
def launch_sig():
    print("launch_sig")
    device_name = request.args.get('device_name', '') # ?hoge=valueの値を取得
    print(device_name)
    trans_sig(device_name)
    return "ok"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

