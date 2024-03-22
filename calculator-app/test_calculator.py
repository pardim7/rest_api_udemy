import unittest

from calculator import calculator

class TestCalculator(unittest.TestCase):
    def test_operation_none(self):
        with self.assertRaises(Exception) as ex:
            calculator(None, 2, 2)
        self.assertEqual(ex.exception.args[0], 'Operação não pode ser nulo')

    def test_invalid_numbers(self):
        with self.assertRaises(Exception) as ex:
            calculator('add', None, 2)
        self.assertEqual(
            ex.exception.args[0], 'Informe dois números válidos para realizar a operação')
        with self.assertRaises(Exception) as ex2:
            calculator('add', 2, None)
        self.assertEqual(
            ex2.exception.args[0], 'Informe dois números válidos para realizar a operação')        

    def test_is_operation_valid(self):
        with self.assertRaises(Exception) as ex:
            calculator('fatorial', 10, 2)
        self.assertEqual(ex.exception.args[0], 'Informe uma operação válida (add, sub, mult, div)')


if __name__ ==  '__main__':
    unittest.main()