from services.main import AppService
from services.escalas import EscalasService
from services.aereoPuerto import AereoPuertoService
from services.piloto import PilotoService

from daos.avion_dao import AvionCRUD

from utils.service_result import ServiceResult, handle_result
from utils.app_exceptions import AppException

class AvionService(AppService):

    def crear(self, item) -> ServiceResult:
        handle_result(AereoPuertoService(self.db).get_by_id(item.origen_id))
        handle_result(AereoPuertoService(self.db).get_by_id(item.destino_id))
        handle_result(PilotoService(self.db).get_by_id(item.piloto_id))
        if (item.origen_id == item.destino_id):
            return ServiceResult(AppException.Avion({'detail': 'El lugar de origen debe de ser diferente al de destino'}))
        if (int(item.cap_max_pasajeros) < 10):
            return ServiceResult(AppException.Avion({'detail': 'La capacidad de passajeros debe de superar 10'}))
        if (item.llegada < item.salida):
            return ServiceResult(AppException.Avion({'detail': 'La fecha de salida, debe de ser menor a la de llegada'}))

        escalas = item.escalas is not None
        if (escalas):
            handle_result(EscalasService(self.db).validar(item.escalas))
        avion = AvionCRUD(self.db).crear(item, escalas)

        if (escalas):
            EscalasService(self.db).crear(item.escalas, avion.id)

        return ServiceResult({"msg": "Avion creado exitosamente"})
    