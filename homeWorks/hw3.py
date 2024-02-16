class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        money = int(input("введите количество денег :"))
        self._balance += money
        return self._balance

    def kill(self):
        return self._balance - self._balance

    def __jackpot(self):
        return self._balance * 10

    def _add_balance(self, our_balance):
        return self._balance + our_balance


