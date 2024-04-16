import csv
from tabulate import tabulate

filename = '../security_logs.csv'

# فتح الملف CSV للقراءة
with open(filename, 'r') as file:
    reader = csv.reader(file)

    # قراءة الصف الأول (رأس الجدول)
    header = next(reader)

    # قائمة لتخزين متغيرات العمود
    variables = []

    # تحليل الصفوف الباقية والتعرف على المتغيرات
    for row in reader:
        variables.append(row)

print('متغيرات الملف:')
for variable in variables:
    print(variable)

print('رأس الجدول:')
print(header)
