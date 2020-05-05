from unittest.mock import Mock
from repositories import SurveyRepository, SurveyResponseRepository
import uuid


def get_mocked_survey_repo():
    repo = SurveyRepository()
    repo.get_all = Mock(name='get_all')
    repo.get_all.return_value = get_list_of_two_surveys()
    repo.get_by_user_id = Mock(name='get_by_user_id')
    repo.get_by_user_id.return_value = get_list_surveys_of_same_user()
    repo.add = Mock(name='add')
    repo.add.return_value = uuid.UUID("06335e84-2832-4914-8c5d-3ed07d2a2f11")
    return repo


def get_empty_mocked_survey_repo():
    repo = SurveyRepository()
    repo.get_all = Mock(name='get_all')
    repo.get_all.return_value = []
    return repo


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
