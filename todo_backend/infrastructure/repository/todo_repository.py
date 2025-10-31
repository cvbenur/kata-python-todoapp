import logging

from todo_backend.infrastructure.dao.todo_dao import TodoDao

class TodoRepository:
    def __init__(self, db_session):
        self.db = db_session
        self.logger = logging.getLogger("TodoRepository")

    def get_all(self):
        ret = self.db.query(TodoDao).all()
        self.logger.debug("Found {} items".format(len(ret)))
        return ret

    def get_one_by_id(self, todo_id: str):
        ret = self.db.query(TodoDao).filter(TodoDao.id == todo_id).first()
        self.logger.info("Found todo with id {}".format(ret.id))
        return ret

    def create(self, text: str):
        to_save = TodoDao(text=text, done=False)
        self.logger.debug("Saving item {}".format(to_save.__dict__))
        self.db.add(to_save)
        self.db.commit()
        self.logger.debug("Item saved")
        return to_save

    def update(self, todo_id: str, text: str, done: bool):
        to_update = self.db.query(TodoDao).filter(TodoDao.id == todo_id).first()
        if to_update is None:
            self.logger.debug("Item not found for id {}".format(todo_id))
            return None
        self.logger.debug("Found item for id {}, updating".format(todo_id))
        to_update.text = text
        to_update.done = done
        self.db.commit()
        self.logger.debug("Item updated")
        return to_update

    def delete_one_by_id(self, todo_id: str):
        to_delete = self.db.query(TodoDao).filter(TodoDao.id == todo_id).first()
        if to_delete is None:
            self.logger.debug("Item not found for id {}".format(todo_id))
            return None
        self.logger.debug("Found item with id {}, deleting".format(todo_id))
        self.db.delete(to_delete)
        self.db.commit()
        self.logger.debug("Item deleted")
        return to_delete