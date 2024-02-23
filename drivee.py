from geopy.distance import geodesic


def assign_orders(orders, couriers):
    for courier in couriers:
        courier['assigned_orders'] = []

    # Создаем копию списка курьеров для отслеживания доступных курьеров
    available_couriers = couriers[:]

    for order in orders:
        min_distance = float('inf')
        closest_courier = None

        # Ищем ближайшего курьера к текущему заказу
        for courier in available_couriers:
            distance = geodesic(order['from'], courier['location']).kilometers
            if distance < min_distance:
                min_distance = distance
                closest_courier = courier

        if closest_courier:
            closest_courier['assigned_orders'].append(order)
            available_couriers.remove(closest_courier)


# заказы
orders = [
    {'from': (62.026251, 129.729165), 'to': (62.049154, 129.741279), 'cost': 50},

    # Добавьте другие заказы
]
# курьеры
couriers = [
    {'location': (62.031029, 129.738542), 'assigned_orders': []},
    {'location': (62.033180, 129.744776), 'assigned_orders': []},
    # Добавьте других курьеров
]

assign_orders(orders, couriers)


for courier_num, courier in enumerate(couriers, start=1):
    print(f"Курьер {courier_num}:")
    for assigned_order in courier['assigned_orders']:
        print(f" - Заказ: От {assigned_order['from']} до {assigned_order['to']}, Стоимость: {assigned_order['cost']} ")
