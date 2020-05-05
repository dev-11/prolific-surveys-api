from repositories import SurveyResponseRepository
from services import SurveyService


class SurveyResponseService:
    def __init__(self, repo: SurveyResponseRepository, survey_service: SurveyService):
        self._repo = repo
        self._survey_service = survey_service

    def add(self, survey_response):
        survey_id = survey_response['survey_id']
        if self._survey_service.has_item(survey_id) and self._survey_service.has_available_places(survey_id):
            self._survey_service.decrease_available_places(survey_id, 1)
            return self._repo.add(survey_response)

        raise ValueError('Cannot add survey response')

    def get_by_survey_id(self, survey_id):
        return self._repo.get_by_survey_id(survey_id)

    def get_by_user_id(self, user_id):
        return self._repo.get_by_user_id(user_id)
