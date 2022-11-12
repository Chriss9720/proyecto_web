from models.foo import FooItem
from schemas.foo import FooItemCreate
from services.main import AppCRUD

class FooCRUD(AppCRUD):

    def get_item(self, id: int) -> FooItem:
        foo_item = self.db.query(FooItem).filter(FooItem.id == id).first()
        if foo_item:
            return foo_item
        return None

    def get_all(self) -> FooItem:
        foo_all = self.db.query(FooItem).all()
        if foo_all:
            return foo_all
        return None

    def create_item(self, item: FooItemCreate) -> FooItem:
        foo_item = FooItem(description=item.description, public=item.public)
        self.db.add(foo_item)
        self.db.commit()
        self.db.refresh(foo_item)
        return foo_item
    
    def update_item(self, item: FooItemCreate, foo_item: FooItem) -> FooItem:
        foo_item.description = item.description
        foo_item.public = item.public
        self.db.add(foo_item)
        self.db.commit()
        self.db.refresh(foo_item)
        return foo_item
    
    def delete_item(self, foo_item: FooItem) -> FooItem:
        self.db.delete(foo_item)
        self.db.commit()
        return foo_item