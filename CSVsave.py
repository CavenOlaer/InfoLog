import csv
import win32evtlog

filename = 'security_logs.csv'

# فتح سجل الأحداث
hand = win32evtlog.OpenEventLog(None, 'Security')

# قراءة السجلات
flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
events = win32evtlog.ReadEventLog(hand, flags, 0)

# كائن CSV للكتابة في الملف
csv_file = open(filename, 'w', newline='')
csv_writer = csv.writer(csv_file)

# كتابة رأس الجدول
header = ['تاريخ', 'وقت', 'مصدر الحدث', 'التصنيف', 'رمز الحدث', 'رسالة الحدث']
csv_writer.writerow(header)

# قراءة وكتابة السجلات في الملف
for event in events:
    event_time = event.TimeGenerated.Format()
    source = event.SourceName
    category = event.EventCategory
    event_id = event.EventID
    message = event.StringInserts

    # تحويل قيم السجلات إلى قائمة
    row = [event_time, source, category, event_id, message]
    csv_writer.writerow(row)

# إغلاق الملف
csv_file.close()

# إغلاق سجل الأحداث
win32evtlog.CloseEventLog(hand)