from flask_restx import Namespace, Resource, reqparse
from services import SurveyResponseServiceFactory


api = Namespace('survey-responses', description='survey responses related operations')

parser = reqparse.RequestParser()
parser.add_argument('survey_id', type=str, location='json')
parser.add_argument('user_id', type=int, location='json')


@api.route('/survey/<string:survey_id>')
class GetSurveyResponsesBySurveyId(Resource):
    def get(self, survey_id):
        srs = SurveyResponseServiceFactory.get_service()
        return srs.get_by_survey_id(survey_id)


@api.route('/user/<int:user_id>')
class GetSurveyResponsesByUserClass(Resource):
    def get(self, user_id):
        srs = SurveyResponseServiceFactory.get_service()
        return srs.get_by_user_id(user_id)


@api.route('/')
class AddSurveyResponse(Resource):

    @api.expect(parser)
    def post(self):
        try:
            srs = SurveyResponseServiceFactory.get_service()
            return srs.add(api.payload)
        except ValueError as e:
            status_code = 500
            response = {
                'statusCode': status_code,
                'error': {
                    'type': 'Exception',
                    'message': e.args
                }
            }

            return response, status_code
