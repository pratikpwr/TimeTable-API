import json
import os

from flask_restful import Resource
from flask import request
from models.timetable_model import TimeTableModel


# noinspection PyBroadException
class TimeTableRes(Resource):

    @staticmethod
    def get(college, branch, std, div):
        file_name = "{}_{}_{}_{}.csv".format(college, branch, std, div)

        tt = TimeTableModel.find_by_tt_name(file_name)
        my_dict = tt.json_string

        final_dict = {
            "college": college,
            "branch": branch,
            "std": std,
            "div": div,
            "timetable": json.loads(my_dict)
        }
        return final_dict

    @staticmethod
    def post(college, branch, std, div):

        json_string = str
        final_dict = {}

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

            tt_dict = TimeTableModel.csv_to_json('./assets/csv_files/{}'.format(file_name))

            final_dict = {
                "college": college,
                "branch": branch,
                "std": std,
                "div": div,
                "timetable": tt_dict
            }
            json_string = json.dumps(tt_dict)

        tt = TimeTableModel.find_by_tt_name(file_name)

        if tt is None:
            tt = TimeTableModel(college=college, branch=branch, div=div, std=std, json_string=json_string,
                                tt_name=file_name)
        else:
            tt.json_string = json_string
        TimeTableModel.save_to_db(tt)
        return final_dict
