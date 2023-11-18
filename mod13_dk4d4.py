import unittest
from datetime import datetime
class TestUserInputs(unittest.TestCase):
    #symbol: capitalized, 1-7 alpha characters
    def test_symbols(self):
        test_data = [
            ('AAPL', True),
            ('GOOGL', True),
            ('123', False),
            ('gOOGL', False),
            ('', False),
        ]

        for symbol, expected_result in test_data:
            with self.subTest(symbol=symbol, expected_result=expected_result):
                result = symbol.isupper() and symbol.isalpha()
                self.assertEqual(result, expected_result, f"Test failed for symbol: {symbol}")
    
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

    #start date: date type YYYY-MM-DD
    def test_valid_start_date(self):
        valid_start_dates = ['2023-11-17']
        for start_date in valid_start_dates:
            with self.subTest(start_date=start_date):
                self.assertTrue(start_date == datetime.strptime(start_date, "%Y-%m-%d").strftime("%Y-%m-%d"), f"Test failed for valid start date: {start_date}")

    def test_invalid_start_date(self):
        invalid_start_dates = ['', '17-11-2023', '-11-2023', '2023/11/17', 'A', 'a', '1']
        for start_date in invalid_start_dates:
            with self.subTest(start_date=start_date):
                try:
                    datetime.strptime(start_date, "%Y-%m-%d")
                    is_valid = True
                except ValueError:
                    is_valid = False

                self.assertFalse(is_valid, f"Test failed for invalid start date: {start_date}")

    #end date: date type YYYY-MM-DD
    def test_valid_end_date(self):
        valid_end_dates = ['2023-11-17']
        for end_date in valid_end_dates:
            with self.subTest(end_date=end_date):
                self.assertTrue(end_date == datetime.strptime(end_date, "%Y-%m-%d").strftime("%Y-%m-%d"), f"Test failed for valid start date: {end_date}")

    def test_invalid_end_date(self):
        invalid_end_dates = ['', '17-11-2023', '-11-2023', '2023/11/17', 'A', 'a', '1']
        for end_date in invalid_end_dates:
            with self.subTest(end_date=end_date):
                try:
                    datetime.strptime(end_date, "%Y-%m-%d")
                    is_valid = True
                except ValueError:
                    is_valid = False

                self.assertFalse(is_valid, f"Test failed for invalid start date: {end_date}")

if __name__ == '__main__':
    unittest.main()
