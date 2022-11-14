from services.main import AppService
from services.escalas import EscalasService

from daos.asiento_dao import AsientoCRUD
from daos.boleto_dao import BoletoRUD
from daos.avion_dao import AvionCRUD

from utils.service_result import ServiceResult, handle_result

class BoletoService(AppService):

    def crear(self, asiento, user) -> ServiceResult:
        BoletoRUD(self.db).crear(asiento, user)
        return ServiceResult({'msg': 'Compra exitosa'})

    def mis_boletos(self, user) -> ServiceResult:
        boletos = BoletoRUD(self.db).mis_boletos(user)
        aviones = {}
        for boleto in boletos:
            asiento = AsientoCRUD(self.db).get(boleto.asiento_id)
            if (asiento.avion_id not in aviones):
                avion = AvionCRUD(self.db).get_by_id(asiento.avion_id)
                aviones[asiento.avion_id] = {
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
                    "folio": avion.folio,
                    "asientos": []
                }
            aviones[asiento.avion_id]['asientos'].append({
                "fila": asiento.fila,
                "columna": asiento.columna,
                "primera_clase": asiento.primera_clase,
                "disponible": asiento.disponible,
                "costo": asiento.costo,
                "id": asiento.id,
                "asiento": asiento.Asiento
            })
        result = []
        for avion in aviones:
            result.append(aviones[avion])
        return ServiceResult({'boletos': result})