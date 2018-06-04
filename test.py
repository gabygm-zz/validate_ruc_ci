# -*- coding: utf-8 -*-
import unittest
from Document import Identifier

class TestIdentifer(unittest.TestCase):

    def test_rules_ci(self):
        self.assertEqual(Identifier.rules_identifier('9999999999'), False)

if __name__ == '__main__':
    unittest.main()