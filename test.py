import unittest
from Document import Identifier

class TestIdentifer(unittest.TestCase):

    def test_convert_roman(self):
        self.assertFalse(Identifier.validate_ci_ruc('12321321312'))


if __name__ == '__main__':
    unittest.main()