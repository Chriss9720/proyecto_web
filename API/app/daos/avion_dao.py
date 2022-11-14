from services.main import AppCRUD

from models.avion import AvionDB

class AvionCRUD(AppCRUD):
    
    def crear(self, item, escalas) -> AvionDB:
        avion = AvionDB (
            folio = "folio",
            cap_max_pasajeros = item.cap_max_pasajeros,
            cap_max_equipaje_kilos = item.cap_max_equipaje_kilos,
            escalas = escalas,
            salida = item.salida,
            llegada = item.llegada,
            filas = item.filas,
            estado = item.estado,
            destino_id_id = item.destino_id,
            origen_id_id = item.origen_id,
            piloto_id = item.piloto_id
        )
        self.db.add(avion)
        self.db.commit()
        self.db.refresh(avion)
        return avion