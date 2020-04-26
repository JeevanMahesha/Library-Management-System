from models.books_model import BookModel
from flask_restful import reqparse,Resource

class BooksResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'AuthorName',
        type=str,
        required=True,
        help='Author Name is required'
    )
    parser.add_argument(
        'BookName',
        type=str,
        required=True,
        help='Author Name is required'
    )
    parser.add_argument(
        'TotalBook',
        type=int,
        required=True,
        help='Author Name is required'
    )
    def post(self):
        requested_data = BooksResource.parser.parse_args()
        if BookModel.find_by_bookname(requested_data['BookName']):
            return {'Message': f'The {requested_data['BookName']} is already stored in database Insted of adding the book increase the total count'}
        book_details = BookModel(**requested_data)
        book_details.save_to_db()
        return {'Message': f'The {requested_data['BookName']} is Added Successfully to DataBase.....'}
