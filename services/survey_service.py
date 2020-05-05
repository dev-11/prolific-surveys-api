from repositories import SurveyRepository


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

    def has_item(self, survey_id):
        try:
            self._repo.get(survey_id)
            return True
        except ValueError:
            return False
