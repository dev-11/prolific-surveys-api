from flask_restx import Namespace, Resource, reqparse
from services import SurveyServiceFactory


api = Namespace('surveys', description='surveys related operations')
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, location='json')
parser.add_argument('available_places', type=int, location='json')
parser.add_argument('user_id', type=int, location='json')


@api.route('/')
class GetSurveys(Resource):
    def get(self):
        service = SurveyServiceFactory.get_service()
        return service.get_all()

    @api.expect(parser)
    def post(self):
        service = SurveyServiceFactory.get_service()
        return service.add_or_update(api.payload)


@api.route('/user/<int:user_id>')
class GetSurveysByUserClass(Resource):
    def get(self, user_id):
        service = SurveyServiceFactory.get_service()
        return service.get_by_user_id(user_id)


