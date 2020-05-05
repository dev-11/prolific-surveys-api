from repositories import SurveyRepository, SurveyResponseRepository


class SurveyService:
    def __init__(self, repo: SurveyRepository):
        self._repo = repo

    def has_available_places(self, survey_id):
        return self._repo.get(survey_id)['available_places'] > 0

    def decrease_available_places(self, survey_id, decrease_amount):
        survey = self._repo.get(survey_id)
        survey['available_places'] -= decrease_amount
        return survey['available_places']

    def add_or_update(self, survey):
        return self._repo.add_or_update(survey)

    def get_all(self):
        return self._repo.get_all()

    def get_by_user_id(self, user_id):
        return self._repo.get_by_user_id(user_id)


class SurveyResponseService:
    def __init__(self, repo: SurveyResponseRepository, survey_service: SurveyService):
        self._repo = repo
        self._survey_service = survey_service

    def add(self, survey_response):
        if self._survey_service.has_available_places(survey_response['survey_id']):
            self._survey_service.decrease_available_places(survey_response['survey_id'], 1)
            return self._repo.add(survey_response)

        raise ValueError('Survey does not have available places')

    def get_by_survey_id(self, survey_id):
        return self._repo.get_by_survey_id(survey_id)

    def get_by_user_id(self, user_id):
        return self._repo.get_by_user_id(user_id)
