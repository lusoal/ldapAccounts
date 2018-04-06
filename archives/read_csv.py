import csv

class Csv(object):

    def __init__(self, csv_path):
        self.csv_path = csv_path

    def return_dict_csv(self):
        dicionario = {"Nome":[],"Sobrenome":[],"Email":[]}
        with open(self.csv_path, "rb") as f:
            reader = csv.reader(f)
            for row in reader:
                try:
                    dicionario["Nome"].append(row[0])
                    dicionario["Sobrenome"].append(row[1])
                    dicionario["Email"].append(row[2])
                except Exception as e:
                    print "Mayne your CSV is not formatted"
        return dicionario
