from services.main import AppCRUD

from models.pais import PaisDB
from models.ciudad import CiudadDB

class PaisEstadoCRUD(AppCRUD):

    def get_paises(self) -> PaisDB:
        return self.db.query(
            PaisDB.id,
            PaisDB.clave.label("code"),
            PaisDB.pais.label("name")
        ).all()

    def estado_by_pais(self, pais_id) -> CiudadDB:
        return self.db.query(
            CiudadDB.id,
            CiudadDB.clave.label("code"),
            CiudadDB.ciudad.label("name")
        ).filter(
            CiudadDB.pais_id == pais_id
        ).all()

    def get_un_estado(self, id) -> CiudadDB:
        return self.db.query(
            CiudadDB.id,
            CiudadDB.clave.label("code"),
            CiudadDB.ciudad.label("name")
        ).filter(
            CiudadDB.id == id
        ).first()