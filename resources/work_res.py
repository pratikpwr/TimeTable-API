from flask_restful import Resource
from flask import request, send_file
from models.work_model import WorkModel
from io import BytesIO


class WorkRes(Resource):

    # two methods required to send assignment data to user

    # 1. only data is send like id and other things
    # list of all work is send acc to user class and div

    # 2. to views timetable in app new get/or any request is done
    # which returns only pdf.
    # take id as parameter for request to search pdf in DB

    @staticmethod
    def get(college, branch, std, div):
        new_list = []
        work_list = WorkModel.find_work_of_requested_user(college=college, branch=branch, std=std, div=div)

        for work in work_list:
            my_dict = {}
            my_dict.setdefault('id', work.id)
            my_dict.setdefault('work_title', work.work_title)
            my_dict.setdefault('work_dec', work.work_desc)
            my_dict.setdefault('subject', work.subject)
            my_dict.setdefault('date', work.date)
            new_list.append(my_dict)

        return {'assignment': new_list}

    # add logic that some fields can be empty like doc, desc
    @staticmethod
    def post(college, branch, std, div):
        work_title = request.form.get('work_title')
        work_desc = request.form.get('work_desc')
        work_date = request.form.get('date')
        subject_name = request.form.get('subject')
        file = request.files['doc']

        work = WorkModel(college=college, branch=branch, std=std, div=div, work_title=work_title, work_desc=work_desc,
                         subject=subject_name, date=work_date, doc=file.read())

        WorkModel.save_work_to_db(work)

        return {'file saved': file.filename}, 201


class WorkDocRes(Resource):

    # return pdf or doc from db based on id
    @staticmethod
    def get(doc_id):
        file_data = WorkModel.find_doc_from_id(doc_id=doc_id)

        return send_file(BytesIO(file_data.doc), attachment_filename='file.pdf', as_attachment=True)
