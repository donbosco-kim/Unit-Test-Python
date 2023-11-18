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
    
    #time series: 1 numeric character, 1 - 4
    def test_valid_time_series(self):
        valid_time_series = ['1', '2', '3', '4']
        for time_series in valid_time_series:
            with self.subTest(time_series=time_series):
                self.assertTrue(time_series.isnumeric() and 1 <= int(time_series) <= 4, f"Test failed for valid time series: {time_series}")

    def test_invalid_time_series(self):
        invalid_time_series = ['', 'a', '%', '1.1']
        for time_series in invalid_time_series:
            with self.subTest(time_series=time_series):
                self.assertFalse(time_series.isnumeric() and 1 <= int(time_series) <= 4, f"Test failed for invalid time series: {time_series}")

if __name__ == '__main__':
    unittest.main()
