"""
I keep app.py very thin.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from credentials import getConfig



app = Flask(__name__)
#app.config.from_object('config.Configuration')

credentials = getConfig()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://'+credentials['db_user']+':'+ \
    credentials['db_pass']+'@docker.moik.org/django'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Here I would set up the cache, a task queue, etc.
