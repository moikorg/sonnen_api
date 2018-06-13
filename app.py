from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from credentials import getConfig
from models import sonnen_sonnenbattery

app = Flask(__name__)

credentials = getConfig()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://'+credentials['db_user']+':'+ \
    credentials['db_pass']+'@docker.moik.org/django'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

# engine = create_engine('mysql+mysqlconnector://root:LSfh3S49iLTTsJr9x2DT@docker.moik.org/django')
# connection = engine.connect()
# result = connection.execute("select * from sonnen_sonnenbattery where id < 10")
# for row in result:
#     print("id :", row['id'])
# connection.close()

@app.route('/')
def hello_world():
    #sonnen_sonnenbattery.query.all()
    something = sonnen_sonnenbattery.query.order_by("id desc").first()
    return 'Hello World! '+str(something.timestamp)

@app.route('/status')
def status():
    status_item = sonnen_sonnenbattery.query.order_by("id desc").first()
    return_str = str(status_item.timestamp)+" consum: "+str(status_item.consumption)
#    return_json = status_item.json()
    return return_str

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/rest/')


if __name__ == '__main__':
    app.run()
