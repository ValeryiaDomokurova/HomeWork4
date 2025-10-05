from homeworks.hw11.bank_deposit.bank import Bank

class CurrencyConverter(Bank):
    def __init__(self, rates=None):
        if rates is None:
            self.rates = {'USD': 3.2677, 'EUR': 3.399, 'BYN': 1.0}
        else:
            self.rates = rates

    def exchange_currency(self, from_curr, amount, to_curr='BYN'):
        if from_curr not in self.rates:
            raise ValueError(f"Unsupported currency: {from_curr}")
        if to_curr not in self.rates:
            raise ValueError(f"Unsupported currency: {to_curr}")
        # Convert from source to BYN, then to target
        amount_in_byn = amount * self.rates[from_curr] if from_curr != 'BYN' else amount
        if to_curr == 'BYN':
            result = amount_in_byn
        else:
            result = amount_in_byn / self.rates[to_curr]
        return (round(result, 2), to_curr)

class Person:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
