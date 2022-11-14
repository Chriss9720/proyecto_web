from services.main import AppService

from daos.aereoPuerto_dao import AereoPuertoCRUD

from utils.service_result import ServiceResult, handle_result
from utils.app_exceptions import AppException

class AereoPuertoService(AppService):

    def crear(self, item) -> ServiceResult:
        AereoPuertoCRUD(self.db).crear(item)
        return ServiceResult({"msg": "Creado exitosamente"})

    def actualizar(self, id, item) -> ServiceResult:
        aereoPuerto_db = handle_result(self.get_by_id(id))
        AereoPuertoCRUD(self.db).actualizar(aereoPuerto_db, item)
        return ServiceResult({"msg": "Actualizacion exitosa"})

    def deleted(self, id) -> ServiceResult:
        aereoPuerto_db = handle_result(self.get_by_id(id))
        AereoPuertoCRUD(self.db).deleted(aereoPuerto_db)
        return ServiceResult({"msg": "Baja exitosa"})

    def get_all(self) -> ServiceResult:
        aereoPuertos = AereoPuertoCRUD(self.db).get_all()
        result = []
        for aereoPuerto in aereoPuertos:
            result.append({
                "ciudad_id": str(aereoPuerto.ciudad_id),
                "nombre": aereoPuerto.nombre,
                "direccion": aereoPuerto.direccion,
                "codigo_postal": aereoPuerto.codigo_postal,
                "id": aereoPuerto.id
            })
        return ServiceResult({'aereo_puertos': result})

    def get_by_estado(self, estado_id):
        aereoPuertos = AereoPuertoCRUD(self.db).get_by_estado(estado_id)
        result = []
        for aereoPuerto in aereoPuertos:
            result.append({
                "ciudad_id": str(aereoPuerto.ciudad_id),
                "nombre": aereoPuerto.nombre,
                "direccion": aereoPuerto.direccion,
                "codigo_postal": aereoPuerto.codigo_postal,
                "id": aereoPuerto.id
            })
        return ServiceResult({'aereo_puertos': result})

    def get_by_id(self, id) -> ServiceResult:
        aereoPuerto_db = AereoPuertoCRUD(self.db).get_by_id(id)
        if (not aereoPuerto_db):
            return ServiceResult(AppException.AereoPuerto({'detail': f'No existe un aereo puerto con el id: {id}'}))
        return ServiceResult(aereoPuerto_db)