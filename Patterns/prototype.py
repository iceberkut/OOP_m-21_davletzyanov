import copy


class OrderPrototype:
    def __init__(self, order_number=None, products=None, total_price=None):
        self.order_number = order_number
        self.products = products
        self.total_price = total_price

    def clone(self):
        return copy.deepcopy(self)


class Order(OrderPrototype):
    def __init__(self, prototype: OrderPrototype):
        super().__init__()
        self.order_number = prototype.order_number
        self.products = prototype.products
        self.total_price = prototype.total_price


######################################################################


prototype_order = OrderPrototype()
prototype_order.order_number = 1001
prototype_order.products = ["Product A", "Product B", "Product C"]
prototype_order.total_price = 150.00

order1 = Order(prototype_order.clone())
order1.order_number = 1002
order1.total_price = 200.00

order2 = Order(prototype_order.clone())
order2.order_number = 1003
order2.products.append("Product D")

print("Order 1:")
print("Order Number:", order1.order_number)
print("Products:", order1.products)
print("Total Price:", order1.total_price)

print("\nOrder 2:")
print("Order Number:", order2.order_number)
print("Products:", order2.products)
print("Total Price:", order2.total_price)
