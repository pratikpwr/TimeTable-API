from flask_restful import Resource
from flask import request, send_file
from models.notice_model import NoticeModel
from io import BytesIO


class NoticeRes(Resource):

    # returns list of notices of selected user
    @staticmethod
    def get(college, branch, std, div):
        new_list = []
        notice_list = NoticeModel.find_notice_of_requested_user(college=college, branch=branch, std=std, div=div)

        for notice in notice_list:
            my_dict = {}
            my_dict.setdefault('id', notice.id)
            my_dict.setdefault('notice_title', notice.notice_title)
            my_dict.setdefault('notice_dec', notice.notice_desc)
            my_dict.setdefault('date', notice.date)
            new_list.append(my_dict)

        return {'assignment': new_list}

    # add logic that some fields can be empty like doc, desc
    # saves the  data and pdf to DB
    @staticmethod
    def post(college, branch, std, div):
        notice_title = request.form.get('notice_title')
        notice_desc = request.form.get('notice_desc')
        notice_date = request.form.get('date')
        file = request.files['doc']

        file_end = file.filename.split('.')[1]

        if file_end not in ['pdf', 'PDF']:
            return {'message': 'Correct Upload PDF file.'}

        work = NoticeModel(college=college, branch=branch, std=std, div=div, notice_title=notice_title,
                           notice_desc=notice_desc, date=notice_date, doc=file.read())

        NoticeModel.save_notice_to_db(work)

        return {'file saved': file.filename}, 201


class NoticeDocRes(Resource):

    # return pdf or doc from db based on id
    @staticmethod
    def get(doc_id):
        file_data = NoticeModel.find_doc_from_id(doc_id=doc_id)
        return send_file(BytesIO(file_data.doc), attachment_filename='file.pdf', as_attachment=True)
