"""
Візьміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
Результат запишіть у файл result_<your_second_name>.csv
"""

import csv

class FileUnion:
    """
    class FileUnion to merge CSV files without duplicates

    Attributes:
    input_files - list of input files
    output_file - result file
    all_rows - list for all rows

    Methods:
    read_files() - read each input file and unite it to all_rows list
    remove_dublicates() - compares rows and write unite rows to unique_rows list
    write_result() - writes the unite rows into the output file

    """

    def __init__(self, input_files, output_file):
        self.input_files = input_files
        self.output_file = output_file
        self.all_rows = []

    def read_files(self):
        for filename in self.input_files:
            with open(filename, newline = '') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    self.all_rows.append(row)

    def remove_dublicates(self):
        unique_rows = []
        for row in self.all_rows:
            if row not in unique_rows:
                unique_rows.append(row)
        self.all_rows = unique_rows

    def write_result(self):
        with open(self.output_file, 'w', newline= '') as csvfile:
            writer = csv.writer(csvfile)
            for row in self.all_rows:
                writer.writerow(row)

files = ['random.csv', 'random-michaels.csv']
result = 'no-dublicate-file.csv'

union = FileUnion(files, result)

union.read_files()

union.remove_dublicates()

union.write_result()