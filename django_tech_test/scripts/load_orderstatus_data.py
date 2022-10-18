from orderstatus.models import Order, OrderDetail
import csv

def run():
    with open('orderstatus/dataset.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header
        rows = [row for row in reader]

        Order.objects.all().delete()
        OrderDetail.objects.all().delete()

        orders = set([row[0] for row in rows])
        for order in orders:
            new_order = Order(order_number=order)
            new_order.save()

        for row in rows:
            order = Order.objects.filter(order_number=row[0]).first()
            print("order",order)
            new_orderline = OrderDetail(order_number=order, item_name = row[1], status = row[2])
            new_orderline.save()
"""         for row in reader:
            print(row)

            genre, _ = Genre.objects.get_or_create(name=row[-1])
            film = Film(title=row[0],
                        year=row[2],
                        genre=genre)
            film.save() """