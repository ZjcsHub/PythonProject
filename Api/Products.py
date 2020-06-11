# coding:utf-8
import flask
from flask import request
from flask import jsonify
import tools

'''
flask： web框架，可以通过flask提供的装饰器@server.route()将普通函数转换为服务
登录接口，需要传url、username、passwd
'''
#创建一个服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)

@server.route('/getProducts',methods=['get'])
def getProducts():
    # 获取通过url请求传参的数据
    # username = request.values.get('name')
    # 获取url请求传的密码，明文
    # pwd = request.values.get('pwd')
    d = {
        "name":"鱼香肉丝",
        "url":"http://pic37.nipic.com/20140113/8800276_184927469000_2.png",
        "price":"￥23.0"
      };
    return jsonify([d])

if __name__ == '__main__':
    server.run(debug=True,port=8080,host='0.0.0.0')

