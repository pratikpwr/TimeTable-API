import csv
from db import db


# noinspection PyBroadException
class TimeModel:
    def __init__(self, college, branch, std, div):
        self.college = college
        self.branch = branch
        self.std = std
        self.div = div

    # temporary method
    @staticmethod
    def csv_to_json(csv_loc):

        my_dict = {}
        try:
            with open(csv_loc) as file:
                reader = csv.reader(file)
                first_row = next(reader)
                for row in reader:
                    day_list = []
                    count = 1
                    while count < len(row):
                        new_period = {}

                        new_period.setdefault('course', row[count].split('/')[0])
                        new_period.setdefault('teacher', row[count].split('/')[1] or "")
                        new_period.setdefault('timeFromHour', first_row[count].split('-')[0].split(':')[0])
                        new_period.setdefault('timeFromMinute', first_row[count].split('-')[0].split(':')[1])
                        new_period.setdefault('timeToHour', first_row[count].split('-')[1].split(':')[0])
                        new_period.setdefault('timeToMinute', first_row[count].split('-')[1].split(':')[1])

                        count += 1
                        day_list.append(new_period)
                        my_dict.setdefault(row[0], day_list)
        except:
            return {"message": "CSV file Not Found"}
        return my_dict
