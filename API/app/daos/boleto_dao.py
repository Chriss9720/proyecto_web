from services.main import AppCRUD

from models.boleto import BoletoDB

class BoletoRUD(AppCRUD):
    
    def crear(self, asiento, user) -> BoletoDB:
        boleto = BoletoDB(
            folio = "folio",
            sub_total = asiento.costo,
            total = asiento.costo*1.22,
            asiento_id = asiento.id,
            usuario_id = user.id
        )
        self.db.add(boleto)
        self.db.commit()
        self.db.refresh(boleto)
        return boleto
