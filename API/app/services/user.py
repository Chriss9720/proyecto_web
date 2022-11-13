from services.main import AppService

from daos.user_dao import UserCRUD

from utils.app_exceptions import AppException
from utils.service_result import ServiceResult
from utils.auth import hash_password

class UserService(AppService):

    def create_user(self, user) -> ServiceResult:

        user.password = hash_password(user.password)
        verify_username = UserCRUD(self.db).get_user_by_username(user.username)
        
        if(verify_username):
            return ServiceResult(AppException.CreateUser({"Message": f"Ya existe un usuario con el username: {user.username}"}))

        user = UserCRUD(self.db).create_user(user)

        if not user:
            return ServiceResult(AppException.CreateUser({"Message": f"No se ha podido crear el User"}))
        
        return ServiceResult(user)
