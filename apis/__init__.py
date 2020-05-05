from flask_restx import Api

from .namespace_surveys import api as ns1
from .namespace_survey_responses import api as ns2

api = Api(
    title='Prolific Survey API',
    version='1.0',
    doc='/doc/'
)

api.add_namespace(ns1)
api.add_namespace(ns2)
