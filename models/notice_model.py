from db import db


class NoticeModel(db.Model):
    __tablename__ = 'notices'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    college = db.Column(db.String)
    branch = db.Column(db.String)
    std = db.Column(db.String)
    div = db.Column(db.String)
    date = db.Column(db.String)
    notice_title = db.Column(db.String)
    notice_desc = db.Column(db.String)
    doc = db.Column(db.LargeBinary)

    def __init__(self, college, branch, std, div, notice_title, notice_desc, date, doc):
        self.college = college
        self.branch = branch
        self.std = std
        self.div = div
        self.notice_title = notice_title
        self.notice_desc = notice_desc
        self.date = date
        self.doc = doc

    @classmethod
    def find_doc_from_id(cls, doc_id):
        return cls.query.filter_by(id=doc_id).first()

    @classmethod
    def find_notice_of_requested_user(cls, college, branch, std, div):
        return cls.query.filter_by(college=college, branch=branch, std=std, div=div).all()

    def save_notice_to_db(self):
        db.session.add(self)
        db.session.commit()
