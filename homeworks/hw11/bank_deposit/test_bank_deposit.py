import unittest
from .bank import Bank
from .currency import CurrencyConverter


class TestBankDeposit(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        print("Created Bank")

    def test_register_client_already_registered(self):
        self.bank.register_client("007", "James Bond")
        result = self.bank.register_client("007", "James Bond")
        self.assertFalse(result)
        self.assertEqual(self.bank.clients["007"]["name"], "James Bond")
        print("Client already registered")

    def test_register_new_client(self):
        result = self.bank.register_client("007", "James Bond")
        self.assertTrue(result)
        self.assertEqual(self.bank.clients["007"]["name"], "James Bond")
        print("New client registered")

    def test_open_deposit(self):
        self.bank.register_client("007", "James Bond")
        result = self.bank.open_deposit_account("007", 1000, 1)
        self.assertTrue(result)
        self.assertEqual(self.bank.clients["007"]["name"], "James Bond")
        print("Deposit opened successfully")

    def test_open_deposit_unregistered(self):
        result = self.bank.open_deposit_account("007", 1000, 1)
        self.assertFalse(result)
        print("The client is unregistered")

    def test_calc_interest_rate(self):
        self.bank.register_client("007", "James Bond")
        self.bank.open_deposit_account("007", 1000, 1)
        result = self.bank.calc_interest_rate(client_id="007")
        expected = 1000 * (1 + 0.1 / 12) ** (1 * 12)
        self.assertEqual(result, round(expected, 2))
        print("Interest rate calculated successfully")

    def test_calc_interest_rate_unregistered(self):
        result = self.bank.calc_interest_rate(client_id="007")
        self.assertFalse(result)
        print("The client is unregistered")

    def test_calc_interest_rate_no_deposit(self):
        self.bank.register_client("007", "James Bond")
        result = self.bank.calc_interest_rate(client_id="007")
        self.assertFalse(result)
        print("The client has no deposit")

    def test_close_deposit(self):
        self.bank.register_client("007", "James Bond")
        self.bank.open_deposit_account("007", 1000, 1)
        expected = self.bank.calc_interest_rate(client_id="007")
        result = self.bank.close_deposit(client_id="007")
        self.assertEqual(result, expected)
        self.assertEqual(self.bank.clients["007"]["name"], "James Bond")
        print("Deposit closed successfully")

    def test_close_deposit_unregistered(self):
        result = self.bank.close_deposit(client_id="007")
        self.assertFalse(result)
        print("The client is unregistered")

    def test_close_deposit_no_deposit(self):
        self.bank.register_client("007", "James Bond")
        result = self.bank.close_deposit(client_id="007")
        self.assertFalse(result)
        print("The client has no deposit")


class TestCurrencyConverter(unittest.TestCase):
    def setUp(self):
        self.converter = CurrencyConverter()
        print("Created Currency Converter")

    def test_convert_usd_by_byn(self):
        result = self.converter.convert("USD", 100)
        expected = 100 * 3.2677
        self.assertEqual(result, expected)
        print("Converted USD to BYN")

    def test_convert_byn_by_eur(self):
        result = self.converter.convert("BYN", 100, "EUR")
        expected = 100 / 3.399
        self.assertEqual(result, round(expected, 2))
        print("Converted BYN to EUR")

    def test_convert_eur_by_usd(self):
        result = self.converter.convert("EUR", 100, "USD")
        eur_to_byn = 100 * 3.399
        expected = eur_to_byn / 3.2677
        self.assertEqual(result, round(expected, 2))
        print("Converted EUR to USD")

    def test_convert_invalid_currency(self):
        with self.assertRaises(ValueError):
            self.converter.convert("RUB", 100)
        print("Invalid currency")


if __name__ == '__main__':
    unittest.main()
