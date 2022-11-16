from services.main import AppService

from daos.piloto_dao import PilotoCRUD

from utils.app_exceptions import AppException
from utils.service_result import ServiceResult, handle_result

class PilotoService(AppService):

    def validar(self, item) -> ServiceResult:
        if (int(item.edad) < 18):
            return ServiceResult(AppException.Piloto({'detail': "El piloto debe de ser mayor a 18 años"}))
        return ServiceResult(item)

    def crear(self, item) -> ServiceResult:
        handle_result(self.validar(item))
        PilotoCRUD(self.db).crear(item)
        return ServiceResult({"msg": "Registro exitoso"})

    def actualizar(self, id, item) -> ServiceResult:
        handle_result(self.validar(item))
        piloto_db = PilotoCRUD(self.db).get(id)
        PilotoCRUD(self.db).actualizar(piloto_db, item)
        return ServiceResult({"msg": "Actualizacion exitosa"})

    def deleted(self, id) -> ServiceResult:
        piloto_db = PilotoCRUD(self.db).get(id)
        PilotoCRUD(self.db).deleted(piloto_db)
        return ServiceResult({"msg": "Eliminado exitoso"})

    def get_all(self) -> ServiceResult:
        pilotos = PilotoCRUD(self.db).get_all()
        result = []
        for piloto in pilotos:
            result.append({
                "nombre": piloto.nombre,
                "edad": str(piloto.edad),
                "experiencia": piloto.experiencia,
                "total_vuelos": piloto.total_vuelos,
                "id": piloto.id
            })
        return ServiceResult({'pilotos':result})

    def get_by_name(self, name) -> ServiceResult:
        pilotos = PilotoCRUD(self.db).get_by_name(name)
        result = []
        for piloto in pilotos:
            result.append({
                "nombre": piloto.nombre,
                "edad": str(piloto.edad),
                "experiencia": piloto.experiencia,
                "total_vuelos": piloto.total_vuelos,
                "id": piloto.id
            })
        return ServiceResult(result)

    def get_by_exp(self, exp) -> ServiceResult:
        pilotos = PilotoCRUD(self.db).get_by_exp(exp)
        result = []
        for piloto in pilotos:
            result.append({
                "nombre": piloto.nombre,
                "edad": str(piloto.edad),
                "experiencia": piloto.experiencia,
                "total_vuelos": piloto.total_vuelos,
                "id": piloto.id
            })
        return ServiceResult(result)

    def get_by_vuelos(self, vuelos) -> ServiceResult:
        pilotos = PilotoCRUD(self.db).get_by_vuelos(vuelos)
        result = []
        for piloto in pilotos:
            result.append({
                "nombre": piloto.nombre,
                "edad": str(piloto.edad),
                "experiencia": piloto.experiencia,
                "total_vuelos": piloto.total_vuelos,
                "id": piloto.id
            })
        return ServiceResult(result)
    
    def get_by_id(self, id) -> ServiceResult:
        piloto = PilotoCRUD(self.db).get_by_id(id)
        if (not piloto):
            return ServiceResult(AppException.Piloto({'detail': f"No existe un piloto con el id {id}"}))
        return ServiceResult({
                "nombre": piloto.nombre,
                "edad": str(piloto.edad),
                "experiencia": piloto.experiencia,
                "total_vuelos": piloto.total_vuelos,
                "id": piloto.id
        })