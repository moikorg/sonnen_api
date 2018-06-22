"""
api imports app, auth and models, but none of these import api.
"""
from flask_restful import Resource, Api

from app import app
from models import sonnen_sonnenbattery


api = Api(app)

class sonnenStatus(Resource):
    def get(self):
        try:
#            status_item = sonnen_sonnenbattery.query.order_by("id desc").get()
            status_item = sonnen_sonnenbattery.query.order_by("id desc").first()
        except Exception as e:
            print (e)
            return {}
        return_json={
            'id': status_item.id,
            'consumption': status_item.consumption,
            'gridFeedIn': status_item.gridConsumption,
            'pacTotal': status_item.pacTotal,
            'production': status_item.production,
            'RSOC': status_item.rsoc,
            'timestamp': str(status_item.timestamp),
            'uAC': status_item.uAC,
            'uBat': status_item.uBat,
            'USOC': status_item.usoc}
        return return_json

api.add_resource(sonnenStatus, '/api/v1/status')
