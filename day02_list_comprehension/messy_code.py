def get_discounted_prices(products):
    discounted = []
    for product in products:
        if product["in_stock"]:
            discounted_price = product["price"] * 0.9
            discounted.append(round(discounted_price, 2))
    return discounted


def get_product_names(products):
    names = []
    for product in products:
        names.append(product["name"].strip().title())
    return names


def get_expensive_names(products, threshold):
    result = []
    for product in products:
        if product["price"] > threshold:
            result.append(product["name"])
    return result
