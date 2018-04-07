import ldap
import ldap.modlist
import string
import random

from notification.send_notify import Email
from mysql.database import Database

class OpenLdap(object):

    def __init__(self, host, cn, dc, dc_final, password):
        self.host = host
        self.cn = cn
        self.dc = dc
        self.dc_final = dc_final
        self.password = password

    def create_connection(self):
        conn = ldap.initialize('ldap://'+self.host)
        #logg as administrator on ldap server
        conn.simple_bind_s("cn="+self.cn+",dc="+self.dc+",dc="+self.dc_final,""+self.password+"")
        ldap_base = "dc="+self.dc+",dc="+self.dc_final
        query = "(uid=TLegal)"
        result = conn.search_s(ldap_base, ldap.SCOPE_SUBTREE, query)
        print result
        return conn

    def add_ldap_user(self,ou,dicionario,conn):
        # db = Database(host="",user="",password="",db="")

        for nome, sobrenome, email in zip(dicionario["Nome"],dicionario["Sobrenome"],dicionario["Email"]):
            chars = string.letters + string.digits + string.punctuation
            pwdSize = 20
            password = ''.join((random.choice(chars)) for x in range(pwdSize))

            uid = str(nome[:1]+sobrenome)
            dn = "uid="+uid+",ou="+ou+",dc="+self.dc+",dc="+self.dc_final
            mod = {
               "objectClass": ["inetOrgPerson", "posixAccount"],
               "uid": [uid],
               "sn": [sobrenome],
               "givenName": [nome],
               "cn": [nome+" "+sobrenome],
               "displayName": [nome+" "+sobrenome],
               "mail":[email],
               "userPassword": [password],
               "uidNumber": ["5000"],
               "gidNumber": ["10000"],
               "loginShell": ["/bin/bash"],
               "homeDirectory": ["/home/"+uid]}

            try:
                e = Email("","")
                result = conn.add_s(dn, ldap.modlist.addModlist(mod))
                e.send_email(password, uid, email)
                #Encrypt Password with MD5

                # db.inserting_users(nome, sobrenome, password, state, uid)
                print result
            except Exception as e:
                print e
