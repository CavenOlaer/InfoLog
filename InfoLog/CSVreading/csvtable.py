import csv
from tabulate import tabulate

filename = '../log_powershell.csv'
delimiter = ','  # استبدل بالفاصلة المناسبة

# قراءة المحتوى من ملف CSV
with open(filename, 'r') as file:
    reader = csv.reader(file, delimiter=delimiter)

    # قراءة الصف الأول (رأس الجدول)
    header = next(reader)

    # قراءة الصفوف الباقية وتخزينها في قائمة
    rows = [row for row in reader]

# عرض الجدول
table = tabulate(rows, headers=header, tablefmt='fancy_grid')
print(table)