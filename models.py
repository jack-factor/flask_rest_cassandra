# -*- coding:utf-8 -*-
import uuid
from cassandra.cluster import Cluster
cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect('bomberman')
# db = CQLAlchemy()


class User():

    def getList():
        return session.execute('SELECT id, email, name, lastname, phone FROM users')

    def getByID(pk):
        query = 'SELECT email, name, lastname, phone FROM users WHERE id=%s'
        future = session.execute_async(query, [pk])
        result = future.result()
        return result[0]

    def save(args):
        pk = uuid.uuid1()
        session.execute('INSERT INTO users (name, lastname, email, phone, id)VALUES (%s, %s, %s, %s, %s)',
                        (args['name'], args['lastname'], args['email'], str(args['phone']), pk))
        return pk

    def update(args):
        pk = args['id']
        session.execute('UPDATE users SET name=%s, lastname=%s, phone=%s ,  email=%s WHERE  id=%s ',
                        (args['name'], args['lastname'], str(args['phone']), args['email'], pk))
        return 'success'

    def delete(pk):
        session.execute('DELETE FROM users WHERE id=%s', [pk])
        return 'success'
