from daos.foo_dao import FooCRUD
from schemas.foo import FooItemCreate, FooItem
from utils.app_exceptions import AppException
from services.main import AppService, AppCRUD
from models.foo import FooItem
from utils.service_result import ServiceResult

class FooService(AppService):

    def get_item(self, id: int) -> ServiceResult:
        foo_item = FooCRUD(self.db).get_item(id)
        if not foo_item:
            return ServiceResult(AppException.FooGetItem({"Message": f"No se ha encontrado ningun objeto con el id: {id}"}))
        if not foo_item.public:
            return ServiceResult(AppException.FooItemRequiresAuth())
        return ServiceResult(foo_item)
    
    def get_all(self) -> ServiceResult:
        foo_all = FooCRUD(self.db).get_all()
        
        if not foo_all:
            return ServiceResult(AppException.FooGetAll({"Message": "No se ha encontrado ningun objeto"}))
        
        for foo_item in foo_all:
            if not foo_item.__dict__.get("public"):
                return ServiceResult(AppException.FooItemRequiresAuth())

        return ServiceResult(foo_all)

    def create_item(self, item: FooItemCreate) -> ServiceResult:
        foo_item = FooCRUD(self.db).create_item(item)
        if not foo_item:
            return ServiceResult(AppException.FooCreateItem({"Message": "No se ha podido crear el objeto"}))
        return ServiceResult(foo_item)

    def update_item(self, id: int, item: FooItemCreate) -> ServiceResult:
        foo_item = FooCRUD(self.db).get_item(id)
        
        if not foo_item:
            return ServiceResult(AppException.FooGetItem({"Message": f"No se ha encontrado ningun objeto con el id: {id}"}))

        foo_item = FooCRUD(self.db).update_item(item, foo_item)
        
        if not foo_item:
            return ServiceResult(AppException.FooUpdateItem({"Message": "No se ha podido actualizar el objeto"}))

        return ServiceResult(foo_item)

    def delete_item(self, id: int) -> ServiceResult:
        foo_item = FooCRUD(self.db).get_item(id)
        
        if not foo_item:
            return ServiceResult(AppException.FooGetItem({"Message": f"No se ha encontrado ningun objeto con el id: {id}"}))

        foo_item = FooCRUD(self.db).delete_item(foo_item)
        
        if not foo_item:
            return ServiceResult(AppException.FooDeleteItem({"Message": "No se ha podido eliminar el objeto"}))

        return ServiceResult(foo_item)
