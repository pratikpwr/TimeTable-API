from flask_restful import Resource
from models.time_model import TimeModel
import json


class Timetable(Resource):

    @staticmethod
    def get(college, branch, std, div):
        file_name = "{}_{}_{}_{}.csv".format(college, branch, std, div)

        tt = TimeModel.find_by_tt_name(file_name)
        my_dict = tt.json_string

        final_dict = {
            "college": college,
            "branch": branch,
            "std": std,
            "div": div,
            "timetable": json.loads(my_dict)
        }
        return final_dict
