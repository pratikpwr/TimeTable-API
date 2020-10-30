from flask_restful import Resource
from flask import request
from models.time_model import TimeModel
import os
import json


# noinspection PyBroadException
class Upload(Resource):

    def post(self):

        json_string = str
        final_dict = {}

        college = request.form.get('college')
        branch = request.form.get('branch')
        std = request.form.get('std')
        div = request.form.get('div')

        file_name = '{}_{}_{}_{}.csv'.format(college, branch, std, div)

        if request.files:
            csv_file = request.files['csv_file']
            try:
                file_end = csv_file.filename.rsplit('.')[1]
            except:
                return {'message': 'Upload Correct file'}

            if file_end not in ['csv', 'CSV']:
                return {'message': 'Upload Correct file'}

            csv_file.save(os.path.join("./assets/csv_files/", file_name))

            tt_dict = TimeModel.csv_to_json('./assets/csv_files/{}'.format(file_name))

            final_dict = {
                "college": college,
                "branch": branch,
                "std": std,
                "div": div,
                "timetable": tt_dict
            }
            json_string = json.dumps(tt_dict)

        tt = TimeModel.find_by_tt_name(file_name)

        if tt is None:
            tt = TimeModel(college=college, branch=branch, div=div, std=std, json_string=json_string,
                           tt_name=file_name)
        else:
            tt.json_string = json_string
        TimeModel.save_to_db(tt)
        return final_dict
