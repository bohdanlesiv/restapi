from db import db


class UserModel(db.Model):
    __tablename__ = 'USERS'

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80))

    password = db.Column(db.String(80))

    def __init__(self, name, password):
        self.username = name
        self.password = password

    def json(self):
        return {'id': self.id,
                'username': self.username}

    @classmethod
    def find_by_user_name(cls, name):
        return cls.query.filter_by(username=name).first()
        #
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # sql = 'SELECT * FROM USERS WHERE USERNAME = ?'
        # result = cursor.execute(sql, (name,))
        # row = result.fetchone()
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        # connection.close()
        # return user

    @classmethod
    def find_user_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # sql = 'SELECT * FROM USERS WHERE ID = ?'
        # result = cursor.execute(sql, (_id,))
        # row = result.fetchone()
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        # connection.close()
        # return user
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

