from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
import configparser

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:xxx@docker.moik.org/django'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

# engine = create_engine('mysql+mysqlconnector://root:LSfh3S49iLTTsJr9x2DT@docker.moik.org/django')
# connection = engine.connect()
# result = connection.execute("select * from sonnen_sonnenbattery where id < 10")
# for row in result:
#     print("id :", row['id'])
# connection.close()

def getConfig():
    config = configparser.ConfigParser()
    config.read('./config.rc')
    credentials = {
        'fn_user':config['Credentials']['username'],
        'fn_pass':config['Credentials']['password'],
    }
    return credentials

class sonnen_sonnenbattery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    consumption = db.Column(db.Integer)
    # gridConsumption:
    #   negativ value = energy consumption from grid
    #   positiv value = energy feed-in to the grid
    gridConsumption = db.Column(db.Integer)
    # pacTotal:
    #   negativ value = battery is charging
    #   postitv value = battery is discharging
    pacTotal = db.Column(db.Integer)
    production = db.Column(db.Integer)
    rsoc = db.Column(db.Integer)
    usoc = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime,nullable=False,index=True)
    uAC = db.Column(db.Integer)
    uBat = db.Column(db.Integer)

@app.route('/')
def hello_world():
    #sonnen_sonnenbattery.query.all()
    something = sonnen_sonnenbattery.query.order_by("id desc").first()
    return 'Hello World! '+str(something.timestamp)

@app.route('/status')
def status():
    status_item = sonnen_sonnenbattery.query.order_by(sonnen_sonnenbattery.id.desc()).first()
    return_str = str(status_item.timestamp)+" consum: "+str(status_item.consumption)
    return_json = status_item.json()
    return return_str

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/rest/')


if __name__ == '__main__':
    app.run()
