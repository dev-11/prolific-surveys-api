from flask_restx import Namespace, Resource
import repositories
import services

api = Namespace('survey-responses', description='survey responses related operations')


@api.route('/survey/<int:survey_id>')
class GetSurveyResponsesBySurveyId(Resource):
    def get(self, survey_id):
        repo = repositories.SurveyRepository()
        ss = services.SurveyService(repo)
        return ss.get_all()


@api.route('/user/<int:user_id>')
class GetSurveyResponsesByUserClass(Resource):
    def get(self, user_id):
        repo = repositories.SurveyRepository()
        ss = services.SurveyService(repo)
        return ss.get_by_user_id(user_id)


@api.route('/<int:survey>')
class AddSurveyResponse(Resource):
    def post(self, survey):
        repo = repositories.SurveyResponseRepository()
        ss = services.SurveyResponseService(repo)
        return ss.add(survey)
