class Items:
    name: str
    id: int
    price: float
    stock: int

    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.id}, {self.name}, price: {self.price}, in stock: {self.stock}"
