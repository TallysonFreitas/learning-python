class Store:

    def __init__(self, name: str, inventory: int, price: float) -> None:
        self.name = name
        self.inventory = inventory
        self.price: float = price

    def buy(self, quantity: int) -> float:
        total: float = 0
        print(f'Voce comprou {quantity} itens na loja {self.name}')
        if quantity == 1:
            total = self.price
            print(f'Nao ha desconto nessa modalidade')

        elif quantity == 2:
            total = self.price + (self.price * 0.7)
            print(f'O desconto nessa modalidade e de 30% para a segunda camisa')

        elif quantity >= 3 and quantity <= 6:
            total = self.price * 2 + (self.price * (quantity - 2) * .5)
            print(f'O desconto nessa modalidade e de 50% para todas camisas a mais que duas')

        elif quantity > 6:
            total = self.price * quantity * .5
            print(f'O desconto nessa modalidade e de 50%')

        print(f'O valor da compra foi de: {round(total, 2)}\n')
        return round(total, 2)


if __name__ == '__main__':
    # create stores
    hearing = Store('hearing', 100000, 129.99)
    americans = Store('americans', 1000000, 49.97)

    # simulate a buy
    hearing.buy(2)
    americans.buy(1)
