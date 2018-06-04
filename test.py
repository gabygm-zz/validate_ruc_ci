# -*- coding: utf-8 -*-
import unittest
from Document import Identifier

class TestIdentifer(unittest.TestCase):

    def test_rules_ci(self):
        self.assertEqual(Identifier.rules_identifier('9999999999'), False)
        self.assertEqual(Identifier.rules_identifier('1105137143'), 0)
        self.assertEqual(Identifier.rules_identifier('1105137143'),0)

    def test_validate_ci(self):
        self.assertFalse(Identifier.validate_ci_ruc('28321321312'))
        self.assertEqual(Identifier.validate_ci_ruc('1105137143'), True)
        self.assertEqual(Identifier.validate_ci_ruc('1105137143001'), True)


if __name__ == '__main__':
    unittest.main()