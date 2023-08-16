import datetime

food_requests = []


def store_message(message):
    # stores message in list
    food_requests.append(message)


def export_list():
    # exports list as txt file every wednesday to food stewards using SMS api

    with open("shopping-lists/list.txt", "w") as list_file:
        for item in food_requests:
            list_file.write(str(item))

    food_requests.clear()
    return
