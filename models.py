from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


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

    #pass
