from services.main import AppCRUD

from models.user import UsersDB

from datetime import datetime

class UserCRUD(AppCRUD):

    def get_user_by_username(self, username: str) -> UsersDB:
        user = self.db.query(UsersDB).where(UsersDB.username == username, UsersDB.deleted == None).first()
        if user:
            return user
        return None    

    def create_user(self, user) -> UsersDB:
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

    def get_by_id(self, id) -> UsersDB:
        return self.db.query(UsersDB).filter(UsersDB.id == id, UsersDB.deleted == None).first()

    def update(self, user_db, user) -> UsersDB:
        user_db.nombre = user.nombre
        user_db.apellido_paterno = user.apellido_paterno
        user_db.apellido_materno = user.apellido_materno
        user_db.correo = user.correo
        user_db.username = user.username
        user_db.password = user.password
        user_db.empleado = user.empleado
        self.db.add(user_db)
        self.db.commit()
        self.db.refresh(user_db)
        return user_db

    def deleted(self, user) -> UsersDB:
        user.deleted = datetime.now()
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user