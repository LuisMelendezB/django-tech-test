from weather.models import WeatherDate
import csv
from datetime import datetime

#Import Weather data from dataset (.csv file)

def run():
    with open('weather/dataset.csv') as file:
        reader = csv.reader(file)
        next(reader)  
        rows = [row for row in reader]

        WeatherDate.objects.all().delete()

        boolean_dict = {'TRUE':True, 'FALSE':False}

        for row in rows:
            new_date = WeatherDate(date = datetime.strptime(row[0],'%m/%d/%y'),
                                    was_rainy = boolean_dict[row[1]])
            new_date.save()