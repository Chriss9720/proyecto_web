from services.main import AppCRUD

from models.escala import EscalasDB

from datetime import datetime

class EscalasCRUD(AppCRUD):
    
    def crear(self, item, avion_id) -> EscalasDB:
        avion = EscalasDB (
            salida = item.salida,
            llegada = item.llegada,
            aereoPuerto_id = int(item.aereoPuerto),
            avion_id = avion_id
        )
        self.db.add(avion)
        self.db.commit()
        self.db.refresh(avion)
        return avion

    def get_escalas(self, avion_id) -> EscalasDB:
        return self.db.query(
            EscalasDB.aereoPuerto_id,
            EscalasDB.salida,
            EscalasDB.llegada
        ).filter(
            EscalasDB.deleted == None,
            EscalasDB.avion_id == avion_id
        ).all()

    def get(self, avion_id) -> EscalasDB:
        return self.db.query(
            EscalasDB
        ).filter(
            EscalasDB.deleted == None,
            EscalasDB.avion_id == avion_id
        ).all()

    def deleted(self, escala_db) -> EscalasDB:
        escala_db.deleted = datetime.now()
        self.db.add(escala_db)
        self.db.commit()
        self.db.refresh(escala_db)
        return escala_db