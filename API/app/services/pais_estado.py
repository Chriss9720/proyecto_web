from services.main import AppService

from daos.pais_estado_dao import PaisEstadoCRUD

from utils.service_result import ServiceResult

class PaisEstadoService(AppService):

    def get_paises(self) -> ServiceResult:
        return ServiceResult({'paises': [pais for pais in PaisEstadoCRUD(self.db).get_paises()]})

    def estado_by_pais(self, pais_id) -> ServiceResult:
        return ServiceResult({'estados': [estado for estado in PaisEstadoCRUD(self.db).estado_by_pais(pais_id)]})