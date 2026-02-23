invoices = [
    {"client": "TechCorp", "status": "Paid", "amount": 1500},
    {"client": "StartupX", "status": "Pending", "amount": 800},
    {"client": "Game_Studio", "status": "Paid", "amount": 2500},
    {"client": "Brothers_Pizza", "status": "Cancelled", "amount": 300},
    {"client": "Cyber_Security_Inc", "status": "Paid", "amount": 4000}
]

def status_check(clients):
    current_status = clients["status"]

    match current_status:
        case "Paid":
            return True
        case _ :
            return False

paid_clients = [*filter(status_check,invoices)]

last_output = [prices["amount"] for prices in paid_clients]

print(last_output)


'''
product_catalog = [
    {"product_name": "Mechanical Keyboard", "stock": 15, "price": 2000},
    {"product_name": "Gaming Mouse", "stock": 0, "price": 800},
    {"product_name": "24-inch Monitor", "stock": 5, "price": 4500},
    {"product_name": "Mousepad", "stock": 0, "price": 200},
    {"product_name": "Headphones", "stock": 12, "price": 1500}
]

def stock_check(product):
    stock = product["stock"]

    if stock == 0 :
        return False
    else:
        return True

def discount(product_for_discount):
    price = product_for_discount["price"]

    new_price = price * 0.9
    product_for_discount["price"] = new_price

    return product_for_discount

avaible_products = [*filter(stock_check, product_catalog)]
last_version = [*map(discount, avaible_products)]


price_list = [price_product["price"] for price_product in last_version]
print(price_list)
'''