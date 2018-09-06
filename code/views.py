"""
views imports app, auth, and models, but none of these import views
"""
from flask import render_template  # ...etc , redirect, request, url_for

from app import app
from models import sonnen_sonnenbattery

@app.route('/')
def hello_world():
    #sonnen_sonnenbattery.query.all()
    try:
        something = sonnen_sonnenbattery.query.order_by("id desc").first()
    except Exception as e:
        retStr = "ERROR! Can not connecto to DB. "+str(e)
        return retStr
    else:
        return 'Hello World! '+str(something.timestamp)

@app.route('/status')
def status():
    try:
        status_item = sonnen_sonnenbattery.query.order_by("id desc").first()
    except Exception as e:
        return "ERROR! Can not connect to DB"
    else:
        return_str = str(status_item.timestamp)+" consum: "+str(status_item.consumption)
#    return_json = status_item.json()
        return return_str
