import csv

# def csv_getter(file : csv):
#     """
#     считывает файл в формате csv, извлекает из него
#
#     """

def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        data = []
        for row in reader:
            data.append(row)
    return header, data

header, data = read_csv('D:\\Corp_summary.csv')
print(header)
for row in data:
    print(row)