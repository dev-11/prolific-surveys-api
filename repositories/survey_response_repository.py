from uuid import uuid4
from datetime import datetime as dt


class SurveyResponseRepository:
    def __init__(self):
        self._survey_responses = []

    def add(self, survey_response):
        survey_response['id'] = str(uuid4())
        survey_response['created_at'] = str(dt.now())
        self._survey_responses.append(survey_response)
        return survey_response['id']

    def get_by_survey_id(self, survey_response_id):
        return list(filter(lambda x: x['survey_id'] == survey_response_id, self._survey_responses))

    def get_by_user_id(self, user_id):
        return list(filter(lambda x: x['user_id'] == user_id, self._survey_responses))
