from services.main import AppCRUD

from models.asiento import AsientoDB

class AsientoCRUD(AppCRUD):
    
    def crear(self, item) -> AsientoDB:
        asiento = AsientoDB(
            columna = item['columna'],
            fila = item['fila'],
            primera_clase = item['primera_clase'],
            Asiento = f"{item['columna']}{item['fila']}",
            costo = item['costo'],
            avion_id = item['avion']
        )
        self.db.add(asiento)
        self.db.commit()
        self.db.refresh(asiento)
        return asiento

    def get_by_columna(self, avion_id, columna) -> AsientoDB:
        return self.db.query(
            AsientoDB.id,
            AsientoDB.columna,
            AsientoDB.fila,
            AsientoDB.Asiento.label('asiento'),
            AsientoDB.primera_clase,
            AsientoDB.costo,
            AsientoDB.disponible,
            AsientoDB.id
        ).filter(
            AsientoDB.columna == columna,
            AsientoDB.deleted == None,
            AsientoDB.disponible,
            AsientoDB.avion_id == avion_id
        ).all()

    def get_by_fila(self, avion_id, columna, fila) -> AsientoDB:
        return self.db.query(
            AsientoDB.id,
            AsientoDB.columna,
            AsientoDB.fila,
            AsientoDB.Asiento.label('asiento'),
            AsientoDB.primera_clase,
            AsientoDB.costo,
            AsientoDB.disponible,
            AsientoDB.id
        ).filter(
            AsientoDB.columna == columna,
            AsientoDB.deleted == None,
            AsientoDB.disponible,
            AsientoDB.avion_id == avion_id,
            AsientoDB.fila == fila
        ).first()

    def get(self, id) -> AsientoDB:
        return self.db.query(
            AsientoDB
        ).filter(
            AsientoDB.id == id
        ).first()

    def comprar(self, asiento) -> AsientoDB:
        asiento.disponible = False
        self.db.add(asiento)
        self.db.commit()
        self.db.refresh(asiento)
        return asiento