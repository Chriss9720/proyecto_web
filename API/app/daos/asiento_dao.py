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