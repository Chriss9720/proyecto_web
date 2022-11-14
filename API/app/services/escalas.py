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
        for item in items.escalas:
            EscalasCRUD(self.db).crear(item, avion_id)
        return ServiceResult(items)

    def get_escalas(self, avion_id) -> ServiceResult:
        result = []
        for escala in EscalasCRUD(self.db).get_escalas(avion_id):
            result.append({
                "aereoPuerto": str(escala.aereoPuerto_id),
                "salida": escala.salida,
                "llegada": escala.salida
            })
        return ServiceResult(result)

    def actualizar(self, avion_id, items) -> ServiceResult:
        for escala in EscalasCRUD(self.db).get(avion_id):
            EscalasCRUD(self.db).deleted(escala)
        self.crear(items, avion_id)
        return ServiceResult({'msg': 'Actualizacion exitosa'})