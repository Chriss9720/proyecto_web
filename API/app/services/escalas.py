from services.main import AppService
from services.aereoPuerto import AereoPuertoService

from daos.escalas_dao import EscalasCRUD

from utils.service_result import ServiceResult
from utils.app_exceptions import AppException

class EscalasService(AppService):

    def validar(self, items) -> ServiceResult:
        for index, item in enumerate(items):
            AereoPuertoService(self.db).get_by_id(item.aereoPuerto)
            if (item.llegada > item.salida):
                return ServiceResult(AppException.Avion({'detail': f'La fecha de llegada, debe de ser menor a la de salida en la escala {index}'}))
        return ServiceResult(items)

    def crear(self, items, avion_id) -> ServiceResult:
        for item in items:
            EscalasCRUD(self.db).crear(item, avion_id)
        return ServiceResult(items)