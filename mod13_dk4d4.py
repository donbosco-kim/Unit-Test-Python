import unittest

class TestUserInputs(unittest.TestCase):
    #symbol: capitalized, 1-7 alpha characters
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
    
    #chart type: 1 numeric character, 1 or 2
    #test for valid charts
    def test_valid_chart(self):
        valid_charts = ['1', '2']
        for chart in valid_charts:
            with self.subTest(chart=chart):
                self.assertTrue(chart.isnumeric(), f"Test failed for chart: {chart}")

    #test for invalid charts
    def test_invalid_chart(self):
        invalid_charts = ['', 'a', '$']
        for chart in invalid_charts:
            with self.subTest(chart=chart):
                self.assertFalse(chart.isnumeric(), f"Test failed for invalid chart: {chart}")

if __name__ == '__main__':
    unittest.main()
