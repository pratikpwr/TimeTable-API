from flask import Flask
from flask_restful import Api
from db import db
import os
from resources.timetable_res import TimeTableRes
from resources.work_res import WorkRes, WorkDocRes
from resources.notice_res import NoticeRes, NoticeDocRes


app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'farCry'


api.add_resource(TimeTableRes, '/timetable/<string:college>/<string:branch>/<string:std>/<string:div>')
api.add_resource(WorkRes, '/work/<string:college>/<string:branch>/<string:std>/<string:div>')
api.add_resource(WorkDocRes, '/work/<doc_id>')
api.add_resource(NoticeRes, '/notice/<string:college>/<string:branch>/<string:std>/<string:div>')
api.add_resource(NoticeDocRes, '/notice/<doc_id>')

if __name__ == '__main__':
    db.init_app(app)

    app.run(debug=True)
