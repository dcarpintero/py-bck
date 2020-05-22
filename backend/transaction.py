import json
import backend.util.bck_math as bck_math
import backend.util.bck_logging as bck_logging

LOGGER = bck_logging.init("dev")


class Transaction:
    """
    Transaction: A transfer of value that is broadcasted to the network and
    collected into blocks. A transaction references previous transaction
    outputs as new transaction inputs and dedicates all input values to
    new outputs. Transactions are not encrypted.
    """
    def __init__(self, vin, vout, value):
        self.vin = vin
        self.vout = vout
        self.value = value
        self.txid = self.compute_hash()

    def compute_hash(self):
        return bck_math.double_hash(self.to_json())

    def to_json(self):
        return json.dumps(self.__dict__, sort_keys=True, indent=2)

    def __repr__(self):
        return self.to_json()
