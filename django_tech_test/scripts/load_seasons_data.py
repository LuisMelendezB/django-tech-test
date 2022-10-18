from seasons.models import CustomerOrder
import csv
from datetime import datetime

#Import Orders data from dataset (.csv file)

def run():
    with open('seasons/dataset.csv') as file:
        reader = csv.reader(file)
        next(reader)  
        rows = [row for row in reader]

        CustomerOrder.objects.all().delete()

        for row in rows:
            date_row = row[2]

            new_orderline = CustomerOrder(ORD_ID=row[0],
                                        ORD_DT = datetime.strptime(row[1], '%m/%d/%y'),
                                        QT_ORDD = row[2])
            new_orderline.save()
