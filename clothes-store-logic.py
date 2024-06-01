class Store:

    def __init__(self, name: str, inventory: int, price: float) -> None:
        self.name = name
        self.inventory = inventory
        self.price: float = price

    def buy(self, quantity: int) -> float:
        total: float = 0
        if quantity == 1:
            total = self.price
            print(f'nao ha desconto nessa modalidade')

        elif quantity == 2:
            total = self.price + (self.price * 0.7)
            print(f'o desconto nessa modalidade e de 30% para a segunda camisa')

        elif quantity >= 3 and quantity <= 6:
            total = self.price * 2 + (self.price * (quantity - 2) * .5)
            print(f'o desconto nessa modalidade e de 50% para todas camisas a mais que duas')

        elif quantity > 6:
            total = self.price * quantity * .5
            print(f'o desconto nessa modalidade e de 50%')

        return round(total, 2)


hearing = Store('Hearing', 100000, 129.87)

print(f'o preco individual de cada peca de roupa e de: {hearing.price}')
print(f'valor final: {hearing.buy(8)}')