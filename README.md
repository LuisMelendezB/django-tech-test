# django-tech-test

## Docker installation example
Run at main directory
```sh
docker build --tag django-tech-test .
docker run --publish 8000:8000 django-tech-test
```

## Local Installation

Install the dependencies and clone django directory

```sh
pip install requirements.txt
python manage.py runserver
```

To restore datasets (if sqlite database is deleted or not cloned):
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runscript load_orderstatus_data
python manage.py runscript load_seasons_data
python manage.py runscript load_weather_data
```


# Endpoints at http://127.0.0.1:8000/
## /orderstatus

You have a data source containing order-line data (each order can have multiple order lines based on the number of products ordered under that specific order). An order line item can be in one of the following three statuses: Pending, Shipped, Cancelled. You want to determine the status of the overall order based on the statuses of each individual order line item for that order. For example, if you have three items in order number 1234, and two of them are marked “Shipped” but one is marked “Pending” then the overall order status is Pending. If all are marked “Shipped” then the Status is “Shipped”.

**Dataset:**
|order_number|item_name|status|
| ------ | ------ | ------ |
|ORD_1567|LAPTOP|SHIPPED|
|ORD_1567|MOUSE|SHIPPED|
|ORD_1567|KEYBOARD|PENDING|
|ORD_1234|GAME|SHIPPED|
|ORD_1234|BOOK|CANCELLED|
|ORD_1234|BOOK|CANCELLED|
|ORD_9834|SHIRT|SHIPPED|
|ORD_9834|PANTS|CANCELLED|
|ORD_7654|TV|CANCELLED|
|ORD_7654|DVD|CANCELLED|

**Expected Result:**
|order_number|status|
| ------ | ------ |
|ORD_1567|PENDING|
|ORD_1234|SHIPPED|
|ORD_9834|SHIPPED|
|ORD_7654|CANCELLED|

## /seasons

You have a table containing a large number of orders over several years - a sample is shown below. Each order has a date attribute that you will need to use to determine the season in which this order was placed. For reference see the table containing the dates in which each season falls.
- Spring: March 19th - June 19th
- Summer: June 20th - September 21st
- Fall: September 22nd - December 20th
- Winter: December 21st - March 18th

**Dataset:**
|ORD_ID|ORD_DT|QT_ORDD|
| ------ | ------ | ------ |
|113-8909896-6940269|9/23/19|1|
|114-0291773-7262677|1/1/20|1|
|114-0291773-7262697|12/5/19|1|
|114-9900513-7761000|9/24/20|1|
|112-5230502-8173028|1/30/20|1|
|112-7714081-3300254|5/2/20|1|
|114-5384551-1465853|4/2/20|1|
|114-7232801-4607440|10/9/20|1|

**Expected Result:**
|ORD_ID|SEASON|
| ------ | ------ |
|113-8909896-6940269|Fall|
|114-0291773-7262697|Fall|
|114-0291773-7262677|Winter|
|114-9900513-7761000|Fall|
|112-5230502-8173028|Winter|
|112-7714081-3300254|Spring|
|114-5384551-1465853|Spring|
|114-7232801-4607440|Fall|

## /weather
You have a table containing data on the weather. Each date has a boolean indicating if it rained (TRUE) or did not rain (FALSE). Query the table to determine the dates in which the weather became bad (i.e. when the weather changed from FALSE to TRUE).

**Dataset:**
|date|was_rainy|
| ------ | ------ |
|1/1/20|FALSE|
|1/2/20|TRUE|
|1/3/20|TRUE|
|1/4/20|FALSE|
|1/5/20|FALSE|
|1/6/20|TRUE|
|1/7/20|FALSE|
|1/8/20|TRUE|
|1/9/20|TRUE|
|1/10/20|TRUE|


**Expected Result:**
|date|was_rainy
| ------ | ------ |
|1/2/20|TRUE|
|1/6/20|TRUE|
|1/8/20|TRUE|
