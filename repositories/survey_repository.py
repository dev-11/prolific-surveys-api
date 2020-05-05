import uuid


class SurveyRepository:
    def __init__(self):
        self._surveys = []

    def add_or_update(self, survey):
        if survey['id'] == 0:
            survey['id'] = uuid.uuid4()
            self._surveys.append(survey)
        else:
            self._surveys.remove(survey)
            self._surveys.append(survey)
        return survey['id']

    def get(self, survey_id):
        return list(filter(lambda x: x.id == survey_id, self._surveys))[0]

    def get_all(self):
        return self._surveys

    def get_by_user_id(self, user_id):
        return list(filter(lambda x: x.user_id == user_id, self._surveys))


class SurveyResponseRepository:
    def __init__(self):
        self._survey_responses = []

    def add(self, survey_response):
        self._survey_responses.append(survey_response)

    def get_by_survey_id(self, survey_id):
        return list(filter(lambda x: x.survey_id == survey_id, self._survey_responses))

    def get_by_user_id(self, user_id):
        return list(filter(lambda x: x.user_id == user_id, self._survey_responses))
