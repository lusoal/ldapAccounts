from open_ldap.open_ldap import OpenLdap
from archives.read_csv import Csv

def main():
    oldap = OpenLdap("","","","","")
    conn = oldap.create_connection()

    csv = Csv("")
    dict_csv = csv.return_dict_csv()

    oldap.add_ldap_user("Users",dict_csv,conn)

if __name__ == '__main__':
    main()
