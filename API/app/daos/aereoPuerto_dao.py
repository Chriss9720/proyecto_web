from services.main import AppCRUD

from models.aereoPuerto import AereoPuertoDB

from datetime import datetime

class AereoPuertoCRUD(AppCRUD):

    def crear(self, item) -> AereoPuertoDB:
        aereoPuerto = AereoPuertoDB(
            nombre = item.nombre,
            direccion = item.direccion,
            codigo_postal = item.codigo_postal,
            ciudad_id = item.ciudad_id
        )
        self.db.add(aereoPuerto)
        self.db.commit()
        self.db.refresh(aereoPuerto)
        return aereoPuerto

    def actualizar(self, aereoPuerto_db, item) -> AereoPuertoDB:
        aereoPuerto_db.nombre = item.nombre
        aereoPuerto_db.direccion = item.direccion
        aereoPuerto_db.codigo_postal = item.codigo_postal
        aereoPuerto_db.ciudad_id = item.ciudad_id
        self.db.add(aereoPuerto_db)
        self.db.commit()
        self.db.refresh(aereoPuerto_db)
        return aereoPuerto_db

    def deleted(self, aereoPuerto_db) -> AereoPuertoDB:
        aereoPuerto_db.deleted = datetime.now()
        self.db.add(aereoPuerto_db)
        self.db.commit()
        self.db.refresh(aereoPuerto_db)
        return aereoPuerto_db

    def get_all(self) -> AereoPuertoDB:
        return self.db.query(
            AereoPuertoDB.ciudad_id,
            AereoPuertoDB.nombre,
            AereoPuertoDB.direccion,
            AereoPuertoDB.codigo_postal,
            AereoPuertoDB.id
        ).filter(
            AereoPuertoDB.deleted == None
        ).all()

    def get_by_estado(self, estado_id) -> AereoPuertoDB:
        return self.db.query(
            AereoPuertoDB.ciudad_id,
            AereoPuertoDB.nombre,
            AereoPuertoDB.direccion,
            AereoPuertoDB.codigo_postal,
            AereoPuertoDB.id
        ).filter(
            AereoPuertoDB.deleted == None,
            AereoPuertoDB.ciudad_id == estado_id
        ).all()

    def get_by_id(self, id) -> AereoPuertoDB:
        return self.db.query(
            AereoPuertoDB
        ).filter(
            AereoPuertoDB.deleted == None,
            AereoPuertoDB.id == id
        ).all()