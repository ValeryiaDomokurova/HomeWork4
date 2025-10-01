class Bank:
    def __init__(self):
        self.clients = {}

    def register_client(self, client_id, name):
        if client_id in self.clients:
            print("Client already registered")
            return False
        else:
            self.clients[client_id] = {"name": name, "deposit": None}
            return True

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id not in self.clients:
            return False

        self.clients[client_id]["deposit"] = {"balance": start_balance, "years": years}
        return True

    def calc_interest_rate(self, client_id):
        if client_id not in self.clients:
            return False
        client = self.clients[client_id]
        if client["deposit"] is None:
            return False

        deposit = client["deposit"]
        balance = deposit["balance"]
        years = deposit["years"]
        rate = balance * (1 + 0.1 / 12) ** (years * 12)
        return round(rate, 2)

    def close_deposit(self, client_id):
        if client_id not in self.clients:
            return False

        client = self.clients[client_id]
        if client["deposit"] is None:
            return False

        final_balance = self.calc_interest_rate(client_id)
        self.clients[client_id]["deposit"] = None

        return final_balance
