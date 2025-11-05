import pytest
import random
import time
from loguru import logger

from homeworks.hw21.source.bank.bank import Bank
from homeworks.hw21.source.bank.currency import CurrencyConverter


class CurrencyConverterStub:
    def __init__(self):
        self.currencies = ["USD", "EUR", "BYN"]
        self.exchange_rates = {
            "USD_BYN": 3.2677,
            "BYN_EUR": 0.2942,
            "EUR_USD": 1.0402,
        }

class CurrencyConverterFake:
    def __init__(self):
        self.rates = {
            "USD": {"BYN": 3.2677, "EUR": 0.9615},
            "EUR": {"BYN": 3.399, "USD": 1.0402},
            "BYN": {"EUR": 0.2942, "USD": 0.306},
        }

    def convert(self, from_curr, amount, to_curr="BYN"):
        if from_curr not in self.rates or to_curr not in self.rates[from_curr]:
            raise ValueError(f"Invalid currency {from_curr} to {to_curr}")
        rate = self.rates[from_curr][to_curr]
        return round(amount * rate, 2)

class BankStub:
    def __init__(self):
        self.name = "Test Bank"
        self.clients = ["007", "008"]
        self.deposit_interest_rate = 0.05

class BankFake:
    def __init__(self):
        self.clients = {}
        self.deposits = {}

    def register_client(self, client_id, name):
        if client_id in self.clients:
            return False
        self.clients[client_id] = name
        return True

    def open_deposit_account(self, client_id, start_balance=1000, years=1):
        if client_id not in self.clients:
            return False
        self.deposits[client_id] = {
            "balance": start_balance,
            "years": years,
        }
        return True

    def calc_interest_rate(self, client_id):
        if client_id not in self.clients:
            return False
        if client_id not in self.deposits:
            return False
        deposit = self.deposits[client_id]
        interest = deposit["balance"] * (1 + 0.05) ** deposit["years"]
        return round(interest, 2)

    def close_deposit(self, client_id):
        if client_id not in self.clients:
            return False
        if client_id not in self.deposits:
            return False
        amount = self.calc_interest_rate(client_id)
        del self.deposits[client_id]
        return amount

    def exchange_currency(self, from_curr, amount, to_curr):
        rates = {
            "USD_BYN": 3.2677,
            "BYN_USD": 0.306,
            "EUR_BYN": 3.399,
            "BYN_EUR": 0.2942,
            "USD_EUR": 0.9615,
            "EUR_USD": 1.0402
        }
        key = f"{from_curr}_{to_curr}"
        if key not in rates:
            raise ValueError(f"Invalid currency {from_curr} to {to_curr}")
        return round(amount * rates[key], 2)

class TestCurrencyConverter:

    @pytest.fixture
    def converter_stub(self):
        return CurrencyConverterStub()

    @pytest.fixture
    def converter_fake(self):
        return CurrencyConverterFake()

    @pytest.fixture
    def converter(self):
        logger.debug("Initializing currency converter")
        return CurrencyConverter()

    def test_converter_stub(self, converter_stub):
        assert "USD" in converter_stub.currencies
        assert "EUR" in converter_stub.currencies
        assert "BYN" in converter_stub.currencies
        assert converter_stub.exchange_rates["USD_BYN"] == 3.2677
        logger.info("Stub: The currency are correct")

    def test_convert_usd_by_byn_fake(self, converter_fake):
        result = converter_fake.convert("USD", 100, "BYN")
        logger.info(f"Fake: Converted USD to BYN: {result}")
        assert result == 326.77

    def test_convert_byn_by_eur_fake(self, converter_fake):
        result = converter_fake.convert("BYN", 100, "EUR")
        logger.info(f"Fake: Converted BYN to EUR: {result}")
        assert result == 29.42

    def test_convert_eur_by_usd_fake(self, converter_fake):
        result = converter_fake.convert("EUR", 100, "USD")
        logger.info(f"Fake: Converted EUR to BYN: {result}")
        assert result == 104.02

    def test_convert_invalid_currency_fake(self, converter_fake):
        with pytest.raises(ValueError):
            converter_fake.convert("RUB", 100, "USD")
        logger.error("Fake: Invalid currency specified")

    def test_converter_called_mock(self, mocker):
        mock_converter = mocker.Mock()
        mock_converter.convert.return_value = 326.77
        result = mock_converter.convert("USD", 100, "BYN")
        logger.info("Mock: Converted USD to BYN")
        assert result == 326.77

    @pytest.mark.flaky(reruns=3, reruns_delay=1)
    def test_unstable_currency_conversion(self, converter_fake):
        time.sleep(random.uniform(0.1, 0.4))

        if random.random() < 0.3:
            logger.info("Unstable test: Skipped")
            assert False

        result = converter_fake.convert("USD", 100, "BYN")
        logger.info("Unstable test: PASSED")
        assert result == 326.77

class TestBank:

    @pytest.fixture
    def bank_stub(self):
        return BankStub()

    @pytest.fixture
    def bank_fake(self):
        return BankFake()

    @pytest.fixture
    def bank(self):
        logger.debug("Initializing bank")
        return Bank()

    @pytest.fixture
    def client_fake(self, bank_fake):
        client_id = "007"
        bank_fake.register_client(client_id, "James Bond")
        return client_id

    def test_bank_stub(self, bank_stub):
        assert bank_stub.name == "Test Bank"
        assert "007" in bank_stub.clients
        assert bank_stub.deposit_interest_rate == 0.05
        logger.info("Stub: The bank are correct")

    def test_register_new_client_fake(self, bank_fake):
        result = bank_fake.register_client("007", "James Bond")
        assert result is True
        assert "007" in bank_fake.clients
        logger.info("Fake: Client registered")

    def test_register_client_already_registered_fake(self, bank_fake):
        bank_fake.register_client("007", "James Bond")
        result = bank_fake.register_client("007", "James Bond")
        logger.info("Fake: Client already registered")
        assert result is False

    def test_open_deposit_fake(self, bank_fake, client_fake):
        result = bank_fake.open_deposit_account(client_fake, 1000, 1)
        logger.info("Fake: Deposit opened")
        assert result is True
        assert client_fake in bank_fake.deposits

    def test_open_deposit_unregistered_fake(self, bank_fake):
        result = bank_fake.open_deposit_account("008", 1000, 1)
        logger.info("Fake: Unregistered client")
        assert result is False

    def test_calc_interest_rate_fake(self, bank_fake, client_fake):
        bank_fake.open_deposit_account(client_fake, 1000, 1)
        result = bank_fake.calc_interest_rate(client_fake)
        logger.info("Fake: Calculated interest rate")
        assert result == 1050.00

    def test_calc_interest_rate_unregistered_fake(self, bank_fake):
        result = bank_fake.calc_interest_rate("008")
        logger.info("Fake: Unregistered client")
        assert result is False

    def test_calc_interest_rate_no_deposit_fake(self, bank_fake, client_fake):
        result = bank_fake.calc_interest_rate(client_fake)
        logger.info("Fake: There isn't a open deposit")
        assert result is False

    def test_close_deposit_fake(self, bank_fake, client_fake):
        bank_fake.open_deposit_account(client_fake, 1000, 1)
        expected = bank_fake.calc_interest_rate(client_fake)
        result = bank_fake.close_deposit(client_fake)
        logger.info("Fake: Deposit closed")
        assert result == expected
        assert client_fake not in bank_fake.deposits

    def test_close_deposit_unregistered_fake(self, bank_fake):
        result = bank_fake.close_deposit("008")
        logger.info("Fake: Unregistered client")
        assert result is False

    def test_close_deposit_no_deposit_fake(self, bank_fake, client_fake):
        result = bank_fake.close_deposit(client_fake)
        logger.info("Fake: There isn't a open deposit")
        assert result is False

    def test_exchange_currency_fake(self, bank_fake):
        result = bank_fake.exchange_currency("USD", 100, "BYN")
        logger.info("Fake: The exchange currency is correct")
        assert result == 326.77

    def test_exchange_currency_invalid_fake(self, bank_fake):
        with pytest.raises(ValueError):
            bank_fake.exchange_currency("RUB", 100, "USD")
        logger.error("Fake: Invalid currency for exchange")

    def test_bank_register_client_mock(self, mocker):
        mock_bank = mocker.Mock()
        mock_bank.register_client("007", "James Bond")
        mock_bank.register_client.assert_called_once_with("007", "James Bond")
        assert mock_bank.register_client.called is True
        assert mock_bank.register_client.call_count == 1
        logger.info("Mock: Client registered")

    def test_bank_open_deposit_mock(self, mocker):
        mock_bank = mocker.Mock()
        mock_bank.open_deposit_account.return_value = True
        result = mock_bank.open_deposit_account("007", 1000, 1)
        mock_bank.open_deposit_account.assert_called_once_with("007", 1000, 1)
        assert result is True
        logger.info("Mock: Deposit opened")
