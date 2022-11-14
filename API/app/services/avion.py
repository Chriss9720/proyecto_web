from services.main import AppService
from services.escalas import EscalasService
from services.aereoPuerto import AereoPuertoService
from services.piloto import PilotoService
from services.asientos import AsientosService

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

        AsientosService(self.db).crear(avion)

        if (escalas):
            EscalasService(self.db).crear(item.escalas, avion.id)

        return ServiceResult({"msg": "Avion creado exitosamente"})

    def get_all(self) -> ServiceResult:
        result = []
        for avion in AvionCRUD(self.db).get_all():
            result.append({
                "cap_max_pasajeros": str(avion.cap_max_pasajeros),
                "cap_max_equipaje_kilos": str(avion.cap_max_equipaje_kilos),
                "origen_id": str(avion.origen_id),
                "destino_id": str(avion.destino_id),
                "escalas": handle_result(EscalasService(self.db).get_escalas(avion.id)),
                "salida": avion.salida,
                "llegada": avion.llegada,
                "filas": str(avion.filas),
                "estado": avion.estado,
                "piloto_id": str(avion.piloto_id),
                "id": avion.id,
                "folio": avion.folio
            })
        return ServiceResult({'aviones': result})

    def get_avion_by_id(self, avion_id):
        avion = AvionCRUD(self.db).get_by_id(avion_id)
        if (not avion):
            return ServiceResult(AppException.Avion({'detail': f'No existe un avion con el id {avion_id}'}))
        result = {
            "cap_max_pasajeros": str(avion.cap_max_pasajeros),
            "cap_max_equipaje_kilos": str(avion.cap_max_equipaje_kilos),
            "origen_id": str(avion.origen_id),
            "destino_id": str(avion.destino_id),
            "escalas": handle_result(EscalasService(self.db).get_escalas(avion.id)),
            "salida": avion.salida,
            "llegada": avion.llegada,
            "filas": str(avion.filas),
            "estado": avion.estado,
            "piloto_id": str(avion.piloto_id),
            "id": avion.id,
            "folio": avion.folio
        }
        return ServiceResult(result)

    def get_bt_origen_destino(self, origen_id, destino_id) -> ServiceResult:
        result = []
        for avion in AvionCRUD(self.db).get_bt_origen_destino(origen_id, destino_id):
            result.append({
                "cap_max_pasajeros": str(avion.cap_max_pasajeros),
                "cap_max_equipaje_kilos": str(avion.cap_max_equipaje_kilos),
                "origen_id": str(avion.origen_id),
                "destino_id": str(avion.destino_id),
                "escalas": handle_result(EscalasService(self.db).get_escalas(avion.id)),
                "salida": avion.salida,
                "llegada": avion.llegada,
                "filas": str(avion.filas),
                "estado": avion.estado,
                "piloto_id": str(avion.piloto_id),
                "id": avion.id,
                "folio": avion.folio
            })
        return ServiceResult({'aviones': result})

    def actualizar(self, avion_id, items) -> ServiceResult:
        avion = AvionCRUD(self.db).get_by_id(avion_id)
        if (not avion):
            return ServiceResult(AppException.Avion({'detail': f'No existe un avion con el id {avion_id}'}))
        return EscalasService(self.db).actualizar(avion.id, items)
