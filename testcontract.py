from unittest import TestCase, skip
from pytezos import MichelsonRuntimeError, ContractInterface

path_to_michelson_contract = "smartcontract.tz"

class TestSmartContract(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.smartContract = ContractInterface.from_file(path_to_michelson_contract)

    def test_storage_5_plus_2_is_7(self):

        # GIVEN
        storage = 5
        value = 2

        # WHEN
        result = self.smartContract.increment(value).interpret(storage=storage,source = 0)

        # THEN
        self.assertEqual(result.storage,7)

    def test_storage_10_minus_7_is_3(self):

        # GIVEN
        storage = 10
        value = 7

        # WHEN
        result = self.smartContract.decrement(value).interpret(storage=storage,source = 0)

        # THEN
        self.assertEqual(result.storage,3)

    def test_storage_25_times_3_is_75(self):

        # GIVEN
        storage = 25
        value = 3

        # WHEN
        result = self.smartContract.multiply(value).interpret(storage=storage,source = 0)

        # THEN
        self.assertEqual(result.storage,75)

    def test_storage_30_divided_by_7_is_4(self):

        # GIVEN
        storage = 30
        value = 7

        # WHEN
        result = self.smartContract.divide(value).interpret(storage=storage,source = 0)

        # THEN
        self.assertEqual(result.storage,4)

    def test_storage_11_modulo_7_is_4(self):
        # GIVEN
        storage = 11
        value = 7

        # WHEN

        result = self.smartContract.modulo(value).interpret(storage=storage,source = 0)
        # THEN
        self.assertEqual(result.storage,4)


    def test_storage_600_reset_is_0(self):
        # GIVEN
        storage = 600

        # WHEN
        result = self.smartContract.reset().interpret(storage=storage,source = 0)
        # THEN
        self.assertEqual(result.storage,0)

