from services.main import AppService

from daos.user_dao import UserCRUD

from utils.app_exceptions import AppException
from utils.service_result import ServiceResult, handle_result
from utils.auth import hash_password

class UserService(AppService):

    def validar(self, user, id) -> ServiceResult:
        if (user):
            verify_username = UserCRUD(self.db).get_user_by_username(user.username)
            if(verify_username and verify_username.id != id):
                return ServiceResult(AppException.User({"Message": f"Ya existe un usuario con el username: {user.username}"}))

        if (id):
            user = UserCRUD(self.db).get_by_id(id)
            if (not user):
                return ServiceResult(AppException.User({"Message": f"No existe un usuario con el id: {id}"}))

        return ServiceResult(user)

    def create_user(self, user) -> ServiceResult:
        user = handle_result(self.validar(user, None))
        user.password = hash_password(user.password)
        user = UserCRUD(self.db).create_user(user)
        return ServiceResult(user)

    def get_by_id(self, id) -> ServiceResult:
        user = handle_result(self.validar(None, id))
        return ServiceResult(user.info_basica())

    def update(self, id, user) -> ServiceResult:
        user_db = handle_result(self.validar(user, id))
        user.password = hash_password(user.password)
        user = UserCRUD(self.db).update(user_db, user)
        return ServiceResult({"msg": "Actualizacion exitosa"})

    def deleted(self, id) -> ServiceResult:
        user = handle_result(self.validar(None, id))
        UserCRUD(self.db).deleted(user)
        return ServiceResult({"msg": "Baja exitosa"})