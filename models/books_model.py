from db_connection import db_connect
import random

class BookModel(db_connect.Model):
    __tablename__ = "allbooks"
    id = db_connect.Column(db_connect.Integer,primary_key=True)
    bookid = db_connect.Column(db_connect.String(20),unique=True)
    authorname = db_connect.Column(db_connect.String(40))
    bookname = db_connect.Column(db_connect.String(40))
    totalbook = db_connect.Column(db_connect.Integer)
    remainingbook = db_connect.Column(db_connect.Integer)

    def __init__(self,AuthorName,BookName,TotalBook):
        self.bookid = 'LMSBOOKID'+str(random.randrange(1111,9999))
        self.authorname = AuthorName
        self.bookname = BookName
        self.totalbook = TotalBook
        self.remainingbook = 0
    
    def save_to_db(self):
        db_connect.session.add(self)
        db_connect.session.commit()

    @classmethod
    def find_by_bookname(cls,bookname):
        return cls.query.filter_by(bookname=bookname).first()

    def delete(self):
        db_connect.session.delete(self)
        db_connect.session.commit()