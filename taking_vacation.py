__author__ = 'payload'


def hotel_cost(nights):
    return 140 * nights


def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475


def rental_car_cost(days):
    if days >= 7:
        return (days * 40) - 50
    elif 2 < days < 7:
        return (days * 40) - 20
    else:
        return days * 40


def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + plane_ride_cost(city) + hotel_cost(days) + spending_money


print trip_cost("Los Angeles", 5, 600)