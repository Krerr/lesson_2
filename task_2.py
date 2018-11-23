import json

file = "orders.json"


def write_order_to_json(item, quantite, price, buer, date):
    data = {
        "item": item,
        "quantite": quantite,
        "price": price,
        "buer": buer,
        "date": date
    }

    with open(file, "r") as f_n:
        try:
            obj = json.load(f_n)
        except Exception:
            print("Невозможно прочитать json файл")
        if("orders" in obj):
            obj["orders"].append(data)
    with open(file, "w") as f_write:
       json.dump(obj, f_write, indent=4)




write_order_to_json(1, 3, 50, 12, "23.03.2018")