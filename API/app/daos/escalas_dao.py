from services.main import AppCRUD

from models.escala import EscalasDB

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