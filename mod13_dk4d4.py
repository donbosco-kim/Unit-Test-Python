import unittest
from datetime import datetime
class TestUserInputs(unittest.TestCase):
    #symbol: capitalized, 1-7 alpha characters
    def test_symbols(self):
        test_symbols = [
            ('AAPL', True),
            ('GOOGL', True),
            ('123', False),
            ('gOOGL', False),
            ('', False),
        ]

        for symbol, expected_result in test_symbols:
            with self.subTest(symbol=symbol, expected_result=expected_result):
                result = symbol.isupper() and symbol.isalpha()
                self.assertEqual(result, expected_result, f"Test failed for symbol: {symbol}")
    
    #chart type: 1 numeric character, 1 or 2
    def test_chart(self):
        test_charts = [
            ('1', True),
            ('2', True),
            ('', False),
            ('a', False),
            ('$', False),
        ]

        for chart, expected_result in test_charts:
            with self.subTest(chart=chart, expected_result=expected_result):
                result = chart.isnumeric()
                self.assertEqual(result, expected_result, f"Test failed for chart: {chart}")
    
    #time series: 1 numeric character, 1 - 4
    def test_time_series(self):
        test_time_series = [
            ('1', True),
            ('2', True),
            ('3', True),
            ('4', True),
            ('', False),
            ('a', False),
            ('%', False),
            ('1.1', False),
        ] 

        for time_series, expected_result in test_time_series:
            with self.subTest(time_series=time_series, expected_result=expected_result):
                result = time_series.isnumeric() and 1 <= int(time_series) <= 4
                self.assertEqual(result, expected_result, f"Test failed for chart: {time_series}")

    #start date: date type YYYY-MM-DD
    def test_start_date(self):
        test_start_date = [
            ('2023-11-17', True),
            ('', False),
            ('17-11-2023', False),
            ('-11-2023', False),
            ('2023/11/17', False),
            ('A', False),
            ('a', False),
            ('1', False),
        ]

        for start_date, expected_result in test_start_date:
            with self.subTest(start_date=start_date, expected_result=expected_result):
                try:
                    datetime.strptime(start_date, "%Y-%m-%d")
                    is_valid = True
                except ValueError:
                    is_valid = False

                self.assertEqual(is_valid, expected_result, f"Test failed for start date: {start_date}")

    #end date: date type YYYY-MM-DD
    #same with start date but here it is anyway
    def test_end_date(self):
        test_end_date = [
            ('2023-11-17', True),
            ('', False),
            ('17-11-2023', False),
            ('-11-2023', False),
            ('2023/11/17', False),
            ('A', False),
            ('a', False),
            ('1', False),
        ]

        for end_date, expected_result in test_end_date:
            with self.subTest(end_date=end_date, expected_result=expected_result):
                try:
                    datetime.strptime(end_date, "%Y-%m-%d")
                    is_valid = True
                except ValueError:
                    is_valid = False

                self.assertEqual(is_valid, expected_result, f"Test failed for start date: {end_date}")

if __name__ == '__main__':
    unittest.main()
