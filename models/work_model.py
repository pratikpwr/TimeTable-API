from db import db


class WorkModel(db.Model):
    __tablename__ = 'works'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    college = db.Column(db.String)
    branch = db.Column(db.String)
    std = db.Column(db.String)
    div = db.Column(db.String)
    date = db.Column(db.String)
    work_title = db.Column(db.String)
    work_desc = db.Column(db.String)
    subject = db.Column(db.String)
    doc = db.Column(db.LargeBinary)

    def __init__(self, college, branch, std, div, work_title, work_desc, subject, date, doc):
        self.college = college
        self.branch = branch
        self.std = std
        self.div = div
        self.work_title = work_title
        self.work_desc = work_desc
        self.subject = subject
        self.date = date
        self.doc = doc

    @classmethod
    def find_doc_from_id(cls, doc_id):
        return cls.query.filter_by(id=doc_id).first()

    @classmethod
    def find_work_of_requested_user(cls, college, branch, std, div):
        return cls.query.filter_by(college=college, branch=branch, std=std, div=div).all()
        pass

    def save_work_to_db(self):
        db.session.add(self)
        db.session.commit()
