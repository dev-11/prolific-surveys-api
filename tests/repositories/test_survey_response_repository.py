import unittest
from repositories import SurveyResponseRepository


class SurveyResponseRepositoryTest(unittest.TestCase):
    def test_get_by_user_id_returns_empty_list_by_default(self):
        sr = SurveyResponseRepository()
        survey_responses = sr.get_by_user_id(1)
        self.assertEqual([], survey_responses)

    def test_get_by_survey_id_returns_empty_list_by_default(self):
        sr = SurveyResponseRepository()
        survey_responses = sr.get_by_survey_id(1)
        self.assertEqual([], survey_responses)

    def test_add_or_update_returns_an_id(self):
        sr = SurveyResponseRepository()
        empty_survey_response = {}
        uuid_str = sr.add(empty_survey_response)
        self.assertTrue(len(uuid_str) > 0)
