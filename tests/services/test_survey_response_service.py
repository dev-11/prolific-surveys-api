import unittest
from services import SurveyResponseService
from tests.test_environment import mocks
import uuid
from datetime import datetime as dt


class TestSurveyResponseService(unittest.TestCase):
    def test_get_by_survey_id_returns_list_with_untouched_items(self):
        srs = SurveyResponseService(mocks.get_mocked_survey_response_repo(), mocks.get_mocked_survey_service(True))
        responses = srs.get_by_survey_id(1)
        self.assertEqual(2, len(responses))
        self.assertEqual(mocks.get_list_of_two_survey_responses_of_survey(),
                         responses)

    def test_get_by_user_id_returns_list_with_untouched_items(self):
        srs = SurveyResponseService(mocks.get_mocked_survey_response_repo(), mocks.get_mocked_survey_service(True))
        responses = srs.get_by_user_id(1)
        self.assertEqual(1, len(responses))
        self.assertEqual(mocks.get_list_of_survey_responses_of_user(), responses)

    def test_add_returns_uuid_when_there_is_available_space(self):
        srs = SurveyResponseService(mocks.get_mocked_survey_response_repo(), mocks.get_mocked_survey_service(True))
        response = srs.add({
            'user_id': 2,
            'created_at': dt(2020, 1, 1, 12, 00, 00),
            'survey_id': 1
        })
        self.assertEqual(uuid.UUID("06335e84-2832-4914-8c5d-3ed07d2a2f12"), response)

    def test_add_raises_exception_when_there_is_no_available_space(self):
        srs = SurveyResponseService(mocks.get_mocked_survey_response_repo(), mocks.get_mocked_survey_service(False))
        self.assertRaises(ValueError, srs.add, {
            'user_id': 2,
            'created_at': dt(2020, 1, 1, 12, 00, 00),
            'survey_id': 1
        })
