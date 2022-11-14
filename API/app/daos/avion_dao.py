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

    def get_all(self):
        return self.db.query(
            AvionDB.cap_max_pasajeros,
            AvionDB.cap_max_equipaje_kilos,
            AvionDB.origen_id_id.label('origen_id'),
            AvionDB.destino_id_id.label('destino_id'),
            AvionDB.salida,
            AvionDB.llegada,
            AvionDB.filas,
            AvionDB.estado,
            AvionDB.piloto_id,
            AvionDB.id,
            AvionDB.folio
        ).filter(
            AvionDB.deleted == None
        ).all()

    def get_by_id(self, id):
        return self.db.query(
            AvionDB.cap_max_pasajeros,
            AvionDB.cap_max_equipaje_kilos,
            AvionDB.origen_id_id.label('origen_id'),
            AvionDB.destino_id_id.label('destino_id'),
            AvionDB.salida,
            AvionDB.llegada,
            AvionDB.filas,
            AvionDB.estado,
            AvionDB.piloto_id,
            AvionDB.id,
            AvionDB.folio
        ).filter(
            AvionDB.deleted == None,
            AvionDB.id == id
        ).first()

    def get_bt_origen_destino(self, origen_id, destino_id):
        return self.db.query(
            AvionDB.cap_max_pasajeros,
            AvionDB.cap_max_equipaje_kilos,
            AvionDB.origen_id_id.label('origen_id'),
            AvionDB.destino_id_id.label('destino_id'),
            AvionDB.salida,
            AvionDB.llegada,
            AvionDB.filas,
            AvionDB.estado,
            AvionDB.piloto_id,
            AvionDB.id,
            AvionDB.folio
        ).filter(
            AvionDB.deleted == None,
            AvionDB.origen_id_id == origen_id,
            AvionDB.destino_id_id == destino_id
        ).all()