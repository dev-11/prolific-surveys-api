from flask_restx import Namespace, Resource
import repositories
import services

api = Namespace('surveys', description='surveys related operations')


class ServiceFactory:
    @staticmethod
    def get_service():
        repo = repositories.SurveyRepository()
        ss = services.SurveyService(repo)
        return ss


@api.route('/')
class GetSurveys(Resource):
    def get(self):
        service = ServiceFactory.get_service()
        return service.get_all()


@api.route('/user/<int:user_id>')
class GetSurveysByUserClass(Resource):
    def get(self, user_id):
        service = ServiceFactory.get_service()
        return service.get_by_user_id(user_id)


@api.route('/<int:user_id>')
class AddSurvey(Resource):
    def post(self, user_id):
        service = ServiceFactory.get_service()
        return service.add(user_id)
