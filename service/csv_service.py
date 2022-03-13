
import csv

class CsvService:

    __writer: csv.writer

    def __init__(self, file_path):
        f =  open(file = file_path, mode = 'w', encoding = 'UTF8')
        self.writer = csv.writer(f)

    def append(self, row):
        self.writer.writerow(row)

    