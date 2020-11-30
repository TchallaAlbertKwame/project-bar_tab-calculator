class Tab:
    menu = {
        'wine': 12,
        'Beer': 20,
        'Chicken': 25,
        'Soft_drink': 22,
        'veggie': 20,
        'Desert': 5,
        'Beef': 11,
        'Pizza': 82,
        'juice': 20

    }

    def __init__(self):
        self.total = 0
        self.items = []

    def add(self, item):
        self.items.append(item)
        self.total += self.menu[item]

    def print_bill(self, tax, service):
        tax = (tax / 100) * self.total
        service = (service / 100) * self.total
        total = self.total + tax + service

        for item in self.items:
            print(f'{item:20} GHC{self.menu[item]}')

        print(f'{"Total":20} GHC{total:.2f}')
