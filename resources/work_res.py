from flask_restful import Resource
from flask import request, send_file
from models.work_model import WorkModel
from io import BytesIO


class WorkRes(Resource):

    # returns list of assignments of selected user
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
    # saves the  data and pdf to DB
    @staticmethod
    def post(college, branch, std, div):
        work_title = request.form.get('work_title')
        work_desc = request.form.get('work_desc')
        work_date = request.form.get('date')
        subject_name = request.form.get('subject')
        file = request.files['doc']

        file_end = file.filename.split('.')[1]

        if file_end not in ['pdf', 'PDF']:
            return {'message': 'Correct Upload PDF file.'}

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
