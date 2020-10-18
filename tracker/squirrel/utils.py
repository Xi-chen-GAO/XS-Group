import csv


class CSV_Opertion:
    def __int__(self):
        pass

    def write(self, path, data_list):
        f = open(path, 'w')
        writer = csv.writer(f)
        for i in data_list:
            writer.writerow(i)
        f.close()

    def read(self, path):
        return csv.reader(open(path))
