class OrderCalculator:

    def __init__(self):
        self._items = []
        self._subtotal = 0

    def get_items(self):
        return self._items

    def add_item(self, item):

        if len(item) != 3:
            raise ValueError("Item must have name, price and quantity")
        if None in item:
            raise ValueError("Item data can't have 'None' values")

        self._items.append(item)

    def calculate_subtotal(self):
        self._subtotal = 0
        for item in self._items:
            self._subtotal = self._subtotal + item[1] * item[2]

        return self._subtotal
