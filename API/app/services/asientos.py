from services.main import AppService
from services.boletos import BoletoService

from daos.asiento_dao import AsientoCRUD

from utils.service_result import ServiceResult
from utils.app_exceptions import AppException

class AsientosService(AppService):

    def crear(self, avion) -> ServiceResult:
        columnas = ['A', 'B', 'C', 'D']
        for fila in range(avion.filas):
            for columna in columnas:
                if (fila < 2):
                    costo = 3000
                else:
                    costo = 1200
                item = {
                    'columna': columna,
                    'fila': fila,
                    'primera_clase': costo == 3000,
                    'costo': costo,
                    'avion': avion.id
                }
                AsientoCRUD(self.db).crear(item)
        return ServiceResult({})

    def comprar(self, items, user) -> ServiceResult:
        for id in items.ids:
            asiento = AsientoCRUD(self.db).get(id.id)
            asiento_db = AsientoCRUD(self.db).comprar(asiento)
            BoletoService(self.db).crear(asiento_db, user)
        return ServiceResult({'msg': 'compra exitosa'})

    def get_by_columna(self, avion_id, columna) -> ServiceResult:
        result = []
        for asiento in AsientoCRUD(self.db).get_by_columna(avion_id, columna):
            result.append({
                "fila": asiento.fila,
                "columna": asiento.columna,
                "primera_clase": asiento.primera_clase,
                "disponible": asiento.disponible,
                "costo": asiento.costo,
                "asiento": asiento.asiento,
                "id": asiento.id
            })
        return ServiceResult({'asientos': result})

    def get_by_id(self, id) -> ServiceResult:
        asiento = AsientoCRUD(self.db).get(id)
        return ServiceResult(asiento)

    def get_by_fila(self, avion_id, columna, fila) -> ServiceResult:
        asiento = AsientoCRUD(self.db).get_by_fila(avion_id, columna, fila)
        if (not asiento):
            return ServiceResult(AppException.Asiento({'detail': 'No existe un asiento con esa informacion'}))
        return ServiceResult({
            "fila": asiento.fila,
            "columna": asiento.columna,
            "primera_clase": asiento.primera_clase,
            "disponible": asiento.disponible,
            "costo": asiento.costo,
            "asiento": asiento.asiento,
            "id": asiento.id
        })