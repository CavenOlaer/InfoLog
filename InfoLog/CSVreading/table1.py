import csv
from prettytable import PrettyTable

filename = '../security_logs.csv'
delimiter = ','  # استبدل بالفاصلة المناسبة

# قراءة المحتوى من ملف CSV
with open(filename, 'r') as file:

    
    reader = csv.reader(file, delimiter=delimiter)

    # قراءة الصف الأول (رأس الجدول)
    header = next(reader)

    # قراءة الصفوف الباقية وتخزينها في قائمة
    rows = [row for row in reader]

# إنشاء كائن جدول
table = PrettyTable(header)

# إضافة الصفوف إلى الجدول
for row in rows:
    table.add_row(row)

# طباعة الجدول
print(table)