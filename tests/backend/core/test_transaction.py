from backend.core.transaction import Transaction


def test_transaction():
    tx = Transaction(vin='0xvin', vout='0xvout', value=111)
    assert isinstance(tx, Transaction)
