from services.main import AppCRUD

from models.piloto import PilotoDB

from datetime import datetime

class PilotoCRUD(AppCRUD):

    def crear(self, item) -> PilotoDB:
        piloto = PilotoDB(
            nombre_completo = item.nombre,
            edad = item.edad,
            experiencia = item.experiencia,
            total_vuelos = item.total_vuelos
        )
        self.db.add(piloto)
        self.db.commit()
        self.db.refresh(piloto)	
        return piloto

    def actualizar(self, piloto_db, item) -> PilotoDB:
        piloto_db.nombre_completo = item.nombre
        piloto_db.edad = item.edad
        piloto_db.experiencia = item.experiencia
        piloto_db.total_vuelos = item.total_vuelos
        self.db.add(piloto_db)
        self.db.commit()
        self.db.refresh(piloto_db)	
        return piloto_db

    def deleted(self, piloto_db) -> PilotoDB:
        piloto_db.deleted = datetime.now()
        self.db.add(piloto_db)
        self.db.commit()
        self.db.refresh(piloto_db)	
        return piloto_db

    def get_all(self) -> PilotoDB:
        return self.db.query(
            PilotoDB.id,
            PilotoDB.edad,
            PilotoDB.experiencia,
            PilotoDB.total_vuelos,
            PilotoDB.nombre_completo.label("nombre")
        ).filter(
            PilotoDB.deleted == None
        ).all()

    def get_by_name(self, name) -> PilotoDB:
        return self.db.query(
            PilotoDB.id,
            PilotoDB.edad,
            PilotoDB.experiencia,
            PilotoDB.total_vuelos,
            PilotoDB.nombre_completo.label("nombre")
        ).filter(
            PilotoDB.nombre_completo == name
        ).all()

    def get_by_exp(self, exp) -> PilotoDB:
        return self.db.query(
            PilotoDB.id,
            PilotoDB.edad,
            PilotoDB.experiencia,
            PilotoDB.total_vuelos,
            PilotoDB.nombre_completo.label("nombre")
        ).filter(
            PilotoDB.experiencia == exp
        ).all()
    
    def get_by_vuelos(self, vuelos) -> PilotoDB:
        return self.db.query(
            PilotoDB.id,
            PilotoDB.edad,
            PilotoDB.experiencia,
            PilotoDB.total_vuelos,
            PilotoDB.nombre_completo.label("nombre")
        ).filter(
            PilotoDB.total_vuelos == vuelos
        ).all()
    
    def get_by_id(self, id) -> PilotoDB:
        return self.db.query(
            PilotoDB.id,
            PilotoDB.edad,
            PilotoDB.experiencia,
            PilotoDB.total_vuelos,
            PilotoDB.nombre_completo.label("nombre")
        ).filter(
            PilotoDB.id == id
        ).first()