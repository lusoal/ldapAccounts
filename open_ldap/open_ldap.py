import ldap
import ldap.modlist
import string
import random
import hashlib

from notification.send_notify import Email
from mysql.database import Database
from config import *

class OpenLdap(object):

    def __init__(self, host, cn, dc, dc_final, password):
        self.host = host
        self.cn = cn
        self.dc = dc
        self.dc_final = dc_final
        self.password = password

    #method to hash a password
    def computeMD5hash(self,my_pass):
        m = hashlib.md5()
        m.update(my_pass.encode('utf-8'))
        return m.hexdigest()

    def create_connection(self):
        conn = ldap.initialize('ldap://'+self.host)
        #logg as administrator on ldap server
        conn.simple_bind_s("cn="+self.cn+",dc="+self.dc+",dc="+self.dc_final,""+self.password+"")
        ldap_base = "dc="+self.dc+",dc="+self.dc_final
        # query = "(mail=)"
        # result = conn.search_s(ldap_base, ldap.SCOPE_SUBTREE, query)
        return conn

    def add_ldap_user(self,ou,dicionario,conn):
        db = Database(host=host_db,user=user_db,password=password_db,db=schema)
        for nome, sobrenome, email in zip(dicionario["Nome"],dicionario["Sobrenome"],dicionario["Email"]):
            chars = string.letters + string.digits + string.punctuation
            pwdSize = 12
            password = ''.join((random.choice(chars)) for x in range(pwdSize))

            uid = str(nome[:1]+sobrenome)
            dn = "uid="+uid+",ou="+ou+",dc="+self.dc+",dc="+self.dc_final
            mod = {
               "objectClass": ["inetOrgPerson","shadowAccount","posixAccount"],
               "uid": [uid],
               "sn": [sobrenome],
               "givenName": [nome],
               "cn": [nome+" "+sobrenome],
               "displayName": [nome+" "+sobrenome],
               "mail":[email],
               "uidNumber": ["5000"],
               "gidNumber": ["10000"],
               "userPassword": [password],
               "loginShell": ["/bin/bash"],
               "homeDirectory": ["/home/"+uid]}

            try:
                e = Email(email_send, password_email)
                result = conn.add_s(dn, ldap.modlist.addModlist(mod))
                e.send_email(password, uid, email)

                #Encrypt Password with MD5
                pwd = self.computeMD5hash(password)
                db.inserting_users(nome, sobrenome, pwd, email, uid)
            except Exception as e:
                print e
