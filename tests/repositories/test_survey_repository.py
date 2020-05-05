import unittest
from repositories import SurveyRepository


class SurveyRepositoryTest(unittest.TestCase):
    def test_get_all_returns_empty_list_by_default(self):
        sr = SurveyRepository()
        every_survey = sr.get_all()
        self.assertEqual([], every_survey)

    def test_add_or_update_returns_an_id(self):
        sr = SurveyRepository()
        empty_survey = {}
        uuid_str = sr.add_or_update(empty_survey)
        self.assertTrue(len(uuid_str) > 0)

    def test_add_or_update_returns_same_id(self):
        sr = SurveyRepository()
        uuid_input = "004b0c5e-e581-4005-abc7-985f71935a6a"
        empty_survey = {"id": uuid_input}
        uuid_str = sr.add_or_update(empty_survey)
        self.assertEqual(uuid_input, uuid_str)

    def test_get_raises_ValueError_by_default(self):
        survey_id = "004b0c5e-e581-4005-abc7-985f71935a6a"
        sr = SurveyRepository()
        self.assertRaises(ValueError, sr.get, survey_id)

    def test_get_by_user_id_returns_empty_list_by_default(self):
        sr = SurveyRepository()
        surveys = sr.get_by_user_id(1)
        self.assertEqual([], surveys)
