import csv
from tabulate import tabulate

filename = '../log_powershell.csv'

with open(filename, 'r') as file:
    reader = csv.reader(file)

    # قراءة الصف الأول (رأس الجدول)
    header = next(reader)

    # قراءة الصفوف الباقية وتخزينها في قائمة
    rows = [row for row in reader]

# عرض الجدول
table = tabulate(rows, headers=header, tablefmt='fancy_grid')
print(table)