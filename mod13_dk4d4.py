import unittest

class TestUserInputs(unittest.TestCase):
    #test for valid symbols
    def test_valid_symbols(self):
        valid_symbols = ['AAPL', 'GOOGL']
        for symbol in valid_symbols:
            with self.subTest(symbol=symbol):
                self.assertTrue(symbol.isupper() and symbol.isalpha(), f"Test failed for symbol: {symbol}")
    
    #test for invalid symbols
    def test_invalid_symbols(self):
        invalid_symbols = ['123', 'gOOGL', '']
        for symbol in invalid_symbols:
            with self.subTest(symbol=symbol):
                self.assertFalse(symbol.isupper() and symbol.isalpha(), f"Test failed for symbol: {symbol}")

if __name__ == '__main__':
    unittest.main()
