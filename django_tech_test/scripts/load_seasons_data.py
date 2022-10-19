from seasons.models import SeasonOrder
import csv
from datetime import datetime

#Import Orders by seasons data from dataset (.csv file)

def run():
    with open('seasons/dataset.csv') as file:
        reader = csv.reader(file)
        next(reader)  
        rows = [row for row in reader]

        SeasonOrder.objects.all().delete()

        for row in rows:
            new_order = SeasonOrder(ORD_ID=row[0],
                                    ORD_DT = datetime.strptime(
                                                                row[1],
                                                                '%m/%d/%y'),
                                    QT_ORDD = row[2])
            new_order.save()
