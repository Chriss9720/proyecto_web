from services.main import AppService

from daos.boleto_dao import BoletoRUD

from utils.service_result import ServiceResult

class BoletoService(AppService):

    def crear(self, asiento, user) -> ServiceResult:
        boleto = BoletoRUD(self.db).crear(asiento, user)
        return ServiceResult({'msg': 'Compra exitosa'})