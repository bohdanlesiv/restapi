from db import db


class ItemModel(db.Model):
    __tablename__ = 'ITEMS'
    id = db.Column(db.Integer, primary_key=True)

    item = db.Column(db.String(80))

    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('STORES.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.item = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.item, 'price': self.price}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # sql_insert_item = 'INSERT INTO ITEMS VALUES(?,?)'
        # cursor.execute(sql_insert_item, (self.item, self.price))
        # connection.commit()
        # connection.close()

    @classmethod
    def get_item_by_name(cls, name):
        return cls.query.filter_by(item=name).first()

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # get_item_sql = 'SELECT * FROM ITEMS WHERE ITEM' \
        #                ' = ?'
        # result = cursor.execute(get_item_sql, (name,))
        # row = result.fetchone()
        # connection.close()
        # if row:
        #     return cls(row[0], row[1])
        #     #return {'item': {'name': row[0], 'price': row[1]}}

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # sql_update_item = 'UPDATE ITEMS SET PRICE = ? WHERE ITEM = ?'
        # cursor.execute(sql_update_item, (self.price, self.item))
        # connection.commit()
        # connection.close()

