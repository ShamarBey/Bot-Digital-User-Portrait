"""
Файл - взаимодействует с базой данных
"""

from peewee import *
from settings.settings import DATABASE, USER, PASSWORD, HOST, PORT

db = PostgresqlDatabase(
    database=DATABASE,
    user=USER,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    autorollback=True,
    autoconnect=True,
)


class User(Model):
    telegram_id = CharField(unique=True)
    user_name = CharField(null=True)

    class Meta:
        database = db
        db_table = 'users'


class MessagesText(Model):
    message_text = CharField(max_length=4000)
    user = ForeignKeyField(User, backref='messages', null=True, on_delete='CASCADE')
    name = CharField(max_length=100)

    class Meta:
        database = db
        db_table = 'messages_text'


def create_tables():
    db.connect()
    db.create_tables([MessagesText, User], safe=True)
    db.close()
