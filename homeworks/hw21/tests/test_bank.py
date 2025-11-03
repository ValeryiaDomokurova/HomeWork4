import pytest
from loguru import logger
from homeworks.hw21.source.bank.bank import Bank
from homeworks.hw21.source.bank.currency import CurrencyConverter


class TestCurrencyConverter:

    @pytest.fixture
    def converter(self):
        logger.debug("Initializing currency converter")
        return CurrencyConverter()

    def test_convert_usd_by_byn(self, converter):
        result = converter.convert("USD", 100, "BYN")
        logger.info(f"Converted USD to BYN: {result}")
        assert result == 326.77

    def test_convert_byn_by_eur(self, converter):
        result = converter.convert("BYN", 100, "EUR")
        logger.info(f"Converted BYN to EUR: {result}")
        assert result == 29.42

    def test_convert_eur_by_usd(self, converter):
        result = converter.convert("EUR", 100, "USD")
        logger.info(f"Converted EUR to BYN: {result}")
        assert result == 104.02

    def test_convert_invalid_currency(self, converter):
        with pytest.raises(ValueError):
            converter.convert("RUB", 100)
        logger.error("Invalid currency specified")

class TestBank:

    @pytest.fixture
    def bank(self):
        logger.debug("Initializing bank")
        return Bank()

    @pytest.fixture
    def client(self, bank):
        client_id = "007"
        client_name = "James Bond"
        bank.register_client(client_id, client_name)
        logger.debug("Client registered")
        return client_id

    def test_register_new_client(self, bank, client):
        assert client in bank.clients
        logger.info("Client registered")

    def test_register_client_already_registered(self, bank, client):
        result = bank.register_client(client, "James Bond")
        logger.info("Client already registered")
        assert result is False

    def test_open_deposit(self, bank, client):
        result = bank.open_deposit_account(client, 1000, 1)
        logger.info(f"Opened deposit: {result}")
        assert result is True

    def test_open_deposit_unregistered(self, bank):
        result = bank.open_deposit_account("008", 1000, 1)
        logger.info("Unregistered client")
        assert result is False

    def test_calc_interest_rate(self, bank, client):
        bank.open_deposit_account(client, 1000, 1)
        result = bank.calc_interest_rate(client)
        logger.info(f"Calculated interest rate: {result}")
        assert result == 1104.71

    def test_calc_interest_rate_unregistered(self, bank):
        result = bank.calc_interest_rate("008")
        logger.info("Unregistered client")
        assert result is False

    def test_calc_interest_rate_no_deposit(self, bank, client):
        result = bank.calc_interest_rate(client)
        logger.info("There isn't a open deposit")
        assert result is False

    def test_close_deposit(self, bank, client):
        bank.open_deposit_account(client, 1000, 1)
        expected = bank.calc_interest_rate(client)
        result = bank.close_deposit(client)
        logger.info("Deposit closed")
        assert result == expected

    def test_close_deposit_unregistered(self, bank):
        result = bank.close_deposit("008")
        logger.info("Unregistered client")
        assert result is False

    def test_close_deposit_no_deposit(self, bank, client):
        result = bank.close_deposit(client)
        logger.info("There isn't a open deposit")
        assert result is False

    def test_exchange_currency(self, bank):
        result = bank.exchange_currency("USD", 100, "BYN")
        logger.info(f"Exchanged currency: {result}")
        assert result == 326.77

    def test_exchange_currency_invalid(self, bank):
        with pytest.raises(ValueError):
            bank.exchange_currency("RUB", 100, "USD")
        logger.error("Invalid currency for exchange")
