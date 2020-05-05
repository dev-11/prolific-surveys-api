from repositories import SurveyRepository, SurveyResponseRepository


class SurveyService:
    def __init__(self, repo: SurveyRepository):
        self._repo = repo

    def add(self, survey):
        return self._repo.add(survey)

    def get_all(self):
        return self._repo.get_all()

    def get_by_user_id(self, user_id):
        return self._repo.get_by_user_id(user_id)


class SurveyResponseService:
    def __init__(self, repo: SurveyResponseRepository):
        self._repo = repo

    def add(self, survey_response):
        return self._repo.add(survey_response)

    def get_all(self, survey_id):
        return self._repo.get_by_survey_id(survey_id)

    def get_by_user_id(self, user_id):
        return self._repo.get_by_user_id(user_id)
