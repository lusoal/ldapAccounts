from open_ldap.open_ldap import OpenLdap
from archives.read_csv import Csv

#set environment vairables for server details
def main():
    oldap = OpenLdap("","Manager","teste","com","123456")
    conn = oldap.create_connection()

    csv = Csv("")
    dict_csv = csv.return_dict_csv()

    oldap.add_ldap_user("Users",dict_csv,conn)

if __name__ == '__main__':
    main()
