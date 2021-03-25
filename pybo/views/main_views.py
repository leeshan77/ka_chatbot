from flask import Blueprint, request, jsonify, render_template
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return 'Hello, Mr.lee welcome to Chatbot!'

@bp.route('/coffe', methods=['POST'])
def coffe():
    req = request.get_json()
    coffe_menu = req['action']['detailParams']['coffe_menu']['value']
    
    answer = coffe_menu
    
    res = {
        'version' : '2.0',
        'template' : {
            'outputs' : [
                {
                    'simpleText' : {
                        'text' : answer
                    }
                }
            ]
        }
    }

    return jsonify(res)
