from sqlalchemy import *
from sqlalchemy.orm import *

class Database(object):

    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def connect_to_db(self):
        try:
            engine = create_engine("mysql://"+self.user+":"+self.password+"@"+self.host+"/"+self.db)
            #creating session
            Session = sessionmaker()
            Session.configure(bind=engine)
            session = Session()
            return session
        except Exception as e:
            return e

    def inserting_users(self, nome, sobrenome, password, state, uid):
        session = connect_to_db()
        if session:
            insert = 'INSERT INTO usuarios(uid, nome, sobrenome, password, state) VALUES('+'"'+uid+'","'+nome+'","'+sobrenome+'","'+password+'","'+state+'")'
            try:
                result_proxy = session.execute(insert)
                session.commit()
            except Exception as e:
                print e
