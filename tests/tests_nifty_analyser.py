import sys
import os
import unittest
import pandas as pd

# Dynamically add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Now import the Nifty 50 Analyzer module
from src.nifty_analyser import fetch_nifty50_data, DATA_PATH, OUTPUT_PATH, PLOT_PATH

class TestNiftyAnalyser(unittest.TestCase):
    """Test cases for the Nifty 50 Analysis script."""

    def test_fetch_nifty50_data(self):
        """Test if fetching Nifty 50 data returns a valid DataFrame."""
        df = fetch_nifty50_data()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)

        required_columns = {'symbol', 'lastPrice', 'previousClose', 'yearHigh', 'yearLow', 'perChange30d'}
        self.assertTrue(required_columns.issubset(df.columns))

    def test_csv_file_creation(self):
        """Test if the stock data CSV file is created."""
        self.assertTrue(os.path.exists(DATA_PATH))

    def test_analysis_output(self):
        """Test if analysis output text file is created."""
        self.assertTrue(os.path.exists(OUTPUT_PATH))
        with open(OUTPUT_PATH, "r", encoding="utf-8") as f:  # Fix warning: specify encoding
            content = f.read()
            self.assertTrue(len(content) > 0)

    def test_plot_file_creation(self):
        """Test if the bar chart plot is created and saved correctly."""
        self.assertTrue(os.path.exists(PLOT_PATH))

if __name__ == '__main__':
    unittest.main()
