from flask_restx import Namespace, Resource
import repositories
import services

api = Namespace('survey-responses', description='survey responses related operations')


@api.route('/survey/<int:survey_id>')
class GetSurveyResponsesBySurveyId(Resource):
    def get(self, survey_id):
        repo = repositories.SurveyResponseRepository()
        ss = services.SurveyService(repositories.SurveyRepository())
        srs = services.SurveyResponseService(repo, ss)
        return srs.get_by_survey_id(survey_id)


@api.route('/user/<int:user_id>')
class GetSurveyResponsesByUserClass(Resource):
    def get(self, user_id):
        repo = repositories.SurveyResponseRepository()
        ss = services.SurveyService(repositories.SurveyRepository())
        srs = services.SurveyResponseService(repo, ss)
        return srs.get_by_user_id(user_id)


@api.route('/<int:survey_response>')
class AddSurveyResponse(Resource):
    def post(self, survey_response):
        repo = repositories.SurveyResponseRepository()
        ss = services.SurveyService(repositories.SurveyRepository())
        srs = services.SurveyResponseService(repo, ss)
        return srs.add(survey_response)
