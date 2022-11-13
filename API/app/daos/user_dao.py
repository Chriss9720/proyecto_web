from schemas.user import User
from models.user import UsersDB
from schemas.user import Credential, UserData
from services.main import AppCRUD

class UserCRUD(AppCRUD):

    def get_user_by_username(self, username: str) -> User:
        user = self.db.query(UsersDB).where(UsersDB.username == username, UsersDB.deleted == None).first()
        if user:
            return user
        return None    

    def create_user(self, user) -> User:
        user = UsersDB(
            nombre = user.nombre,
            apellido_paterno = user.apellido_materno,
            apellido_materno = user.apellido_materno,
            correo = user.correo,
            username = user.username,
            password = user.password,
            empleado = user.empleado
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user