class CurrencyConverter():
    def __init__(self):
        self.rates = {'USD': 3.2677, 'EUR': 3.399, 'BYN': 1.0}

    def convert(self, from_curr, amount, to_curr='BYN'):
        if from_curr not in self.rates:
            raise ValueError(f"Unsupported currency: {from_curr}")
        if to_curr not in self.rates:
            raise ValueError(f"Unsupported currency: {to_curr}")
        # Convert from source to BYN, then to target
        amount_in_byn = amount * self.rates[from_curr]
        amount_from_byn = amount_in_byn / self.rates[to_curr]
        return round(amount_from_byn, 2)
