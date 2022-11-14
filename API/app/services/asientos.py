from services.main import AppService

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