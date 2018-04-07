from open_ldap.open_ldap import OpenLdap
from archives.read_csv import Csv
from config import *

#set environment vairables for server details
def main():
    oldap = OpenLdap(ip_server, root_user, dc_1, dc_2, root_password)
    conn = oldap.create_connection()

    csv = Csv(csv_file)
    dict_csv = csv.return_dict_csv()

    oldap.add_ldap_user(orgarnization_unit, dict_csv, conn)

if __name__ == '__main__':
    main()
