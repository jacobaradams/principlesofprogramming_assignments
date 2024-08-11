class ItemToPurchase:
    def __init__(self, item_name = 'none', item_price = 0, item_quantity = 0):
        self.item_name = str(item_name)
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
    def print_item_cost(self):
        item_total_cost = self.item_price * self.item_quantity
        print(f'{self.item_name} {self.item_quantity} @ {self.item_price:.2f} = ${item_total_cost:.2f}')
Item1 = ItemToPurchase('chocolate chips', 3, 1)
Item1.print_item_cost()