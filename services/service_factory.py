import services
import repositories


class SurveyServiceFactory:
    __ss = None

    @classmethod
    def get_service(cls):
        if cls.__ss is None:
            cls.__ss = services.SurveyService(repositories.SurveyRepository())
        return cls.__ss


class SurveyResponseServiceFactory:
    __srs = None

    @classmethod
    def get_service(cls):
        if cls.__srs is None:
            cls.__srs = services.SurveyResponseService(
                repositories.SurveyResponseRepository(),
                SurveyServiceFactory.get_service())
        return cls.__srs
