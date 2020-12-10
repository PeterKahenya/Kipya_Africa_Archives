import xlrd
import os
from subscribers.models import Subscriber

wb=xlrd.open_workbook('initial.xlsx')
ws=wb.sheet_by_index(0)
for index in range(1,100):
    fullname=ws.cell_value(index,0)
    email=ws.cell_value(index,1)

    s_test=Subscriber.objects.filter(fullname=fullname).first()
    if s_test:
        s_test.delete()
        s=Subscriber()
        s.fullname=fullname
        s.email=email
        s.save()
        print(fullname+"--"+email)
    