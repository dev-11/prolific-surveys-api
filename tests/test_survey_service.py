import unittest
from services import SurveyService
from tests.test_environment import mocks
import uuid


class SurveyServiceTests(unittest.TestCase):
    def test_get_all_returns_empty_list_for_empty_data(self):
        s = SurveyService(mocks.get_empty_mocked_survey_repo())
        surveys = s.get_all()
        self.assertEqual(0, len(surveys))

    def test_get_all_returns_correct_list(self):
        s = SurveyService(mocks.get_mocked_survey_repo())
        surveys = s.get_all()
        self.assertEqual(2, len(surveys))
        self.assertListEqual(mocks.get_list_of_two_surveys(), surveys)

    def test_get_surveys_by_user_id(self):
        s = SurveyService(mocks.get_mocked_survey_repo())
        surveys = s.get_by_user_id(2)
        self.assertEqual(2, len(surveys))
        self.assertListEqual(mocks.get_list_surveys_of_same_user(), surveys)
        self.assertEqual(2, surveys[0]['user_id'])
        self.assertEqual(2, surveys[1]['user_id'])

    def test_add_adds_one_item_and_returns_id(self):
        survey = {
            'id': 0,
            'name': 'test_survey_name',
            'available_places': 1,
            'user_id': 2
        }

        s = SurveyService(mocks.get_mocked_survey_repo())
        survey_id = s.add_or_update(survey)
        self.assertEqual(uuid.UUID("06335e84-2832-4914-8c5d-3ed07d2a2f11"), survey_id)

    def test_has_available_places_returns_true_for_positive_number(self):
        s = SurveyService(mocks.get_mocked_survey_repo())
        has_available_places = s.has_available_places(uuid.UUID("06335e84-2832-4914-8c5d-3ed07d2a2f11"))
        self.assertTrue(has_available_places)

    def test_has_available_places_returns_true_for_zero(self):
        s = SurveyService(mocks.get_mocked_survey_repo(0))
        has_available_places = s.has_available_places(uuid.UUID("06335e84-2832-4914-8c5d-3ed07d2a2f11"))
        self.assertFalse(has_available_places)

    def test_has_available_places_returns_true_for_negative_number(self):
        s = SurveyService(mocks.get_mocked_survey_repo(-1))
        has_available_places = s.has_available_places(uuid.UUID("06335e84-2832-4914-8c5d-3ed07d2a2f11"))
        self.assertFalse(has_available_places)
