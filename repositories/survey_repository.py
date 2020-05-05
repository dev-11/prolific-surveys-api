from uuid import uuid4
import validator as v


class SurveyRepository:
    def __init__(self):
        self._surveys = []

    def add_or_update(self, survey):
        if 'id' not in survey or not v.is_uuid_valid(survey['id']):
            survey['id'] = str(uuid4())
            self._surveys.append(survey)
        else:
            self._surveys.remove(survey)
            self._surveys.append(survey)
        return survey['id']

    def get(self, survey_id):
        survey = list(filter(lambda x: x['id'] == survey_id, self._surveys))
        if len(survey) != 1:
            raise ValueError('data error')
        return survey[0]

    def get_all(self):
        return self._surveys

    def get_by_user_id(self, user_id):
        return list(filter(lambda x: x['user_id'] == user_id, self._surveys))
