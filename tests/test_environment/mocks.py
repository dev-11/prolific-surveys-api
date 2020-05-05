from unittest.mock import Mock
from repositories import SurveyRepository, SurveyResponseRepository
from services import SurveyService
import uuid
from datetime import datetime as dt


def get_mocked_survey_service(has_available_places):
    ss = SurveyService(get_mocked_survey_repo())
    ss.has_available_places = Mock(name='has_available_places')
    ss.has_available_places.return_value = has_available_places
    return ss


def get_mocked_survey_response_repo():
    repo = SurveyResponseRepository()
    repo.get_by_user_id = Mock(name='get_by_user_id')
    repo.get_by_user_id.return_value = get_list_of_survey_responses_of_user()
    repo.get_by_survey_id = Mock(name='get_by_survey_id')
    repo.get_by_survey_id.return_value = get_list_of_two_survey_responses_of_survey()
    repo.add = Mock(name='add')
    repo.add.return_value = uuid.UUID("06335e84-2832-4914-8c5d-3ed07d2a2f12")
    return repo


def get_mocked_survey_repo(available_places=1):
    repo = SurveyRepository()
    repo.get_all = Mock(name='get_all')
    repo.get_all.return_value = get_list_of_two_surveys()
    repo.get_by_user_id = Mock(name='get_by_user_id')
    repo.get_by_user_id.return_value = get_list_surveys_of_same_user()
    repo.add_or_update = Mock(name='add_or_update')
    repo.add_or_update.return_value = uuid.UUID("06335e84-2832-4914-8c5d-3ed07d2a2f11")
    repo.get = Mock(name='get')
    repo.get.return_value = {
        'id': uuid.UUID("06335e84-2832-4914-8c5d-3ed07d2a2f11"),
        'name': 'test_survey_name',
        'available_places': available_places,
        'user_id': 2
    }
    return repo


def get_empty_mocked_survey_repo():
    repo = SurveyRepository()
    repo.get_all = Mock(name='get_all')
    repo.get_all.return_value = []
    return repo


def get_list_of_two_survey_responses_of_survey():
    return [
        {
            'id': uuid.UUID("06335e84-2832-4914-8c5d-3ed07d2a2f11"),
            'user_id': 2,
            'created_at': dt(2020, 1, 1, 12, 00, 00),
            'survey_id': 1
        },
        {
            'id': uuid.UUID("06335e84-7832-4914-8c5d-3ed07d2a2f11"),
            'user_id': 3,
            'created_at': dt(2020, 1, 2, 12, 00, 00),
            'survey_id': 1
        }
    ]


def get_list_of_survey_responses_of_user():
    return [
        {
            'id': uuid.UUID("16335e84-2832-4914-8c5d-3ed07d2a2f11"),
            'user_id': 2,
            'created_at': dt(2020, 1, 1, 12, 00, 00),
            'survey_id': 1
        }
    ]


def get_list_of_two_surveys():
    return [
        {
            'id': uuid.UUID("06335e84-2832-4914-8c5d-3ed07d2a2f11"),
            'name': 'test_survey_name',
            'available_places': 1,
            'user_id': 2
        },
        {
            'id': uuid.UUID("06335e84-2832-4914-8c5d-3ed07d2a2f12"),
            'name': 'test_survey_name 2',
            'available_places': 3,
            'user_id': 4
        }
    ]


def get_list_surveys_of_same_user():
    return [
        {
            'id': uuid.UUID("06335e84-2832-4914-8c5d-3ed07d2a2f11"),
            'name': 'test_survey_name',
            'available_places': 1,
            'user_id': 2
        },
        {
            'id': uuid.UUID("06335e84-2832-4914-8c5d-3ed07d2a2f12"),
            'name': 'test_survey_name 2',
            'available_places': 3,
            'user_id': 2
        }
    ]
