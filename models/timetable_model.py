import csv
from db import db


# noinspection PyBroadException
class TimeTableModel(db.Model):
    __tablename__ = 'timetables'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    college = db.Column(db.String)
    branch = db.Column(db.String)
    std = db.Column(db.String)
    div = db.Column(db.String)
    tt_name = db.Column(db.String)
    json_string = db.Column(db.String)

    def __init__(self, college, branch, std, div, tt_name, json_string):
        self.college = college
        self.branch = branch
        self.std = std
        self.div = div
        self.tt_name = tt_name
        self.json_string = json_string

    @classmethod
    def find_by_tt_name(cls, tt_name):
        return cls.query.filter_by(tt_name=tt_name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

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
