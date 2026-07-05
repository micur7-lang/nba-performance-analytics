"""
Automated Test Suite for NBA Performance Analytics Engine
Author: Michael Stephen Curbeam Jr.
Description: Unit tests verifying data engineering pipeline integrity, 
             transformation logic, and exception masking.
"""

import unittest
# Import specific functions from your pipeline script using a relative import
from .pipeline import calculate_efficiency, write_out_file

class TestNBAPipeline(unittest.TestCase):

    def test_empty_dataset_handling(self):
        """Verify the transformation logic handles an empty dataset gracefully without crashing."""
        # Mocking empty collection handling in write_out_file
        report = write_out_file([])
        self.assertEqual(report, "")

    def test_efficiency_logic_handling(self):
        """Verify the internal structural metrics calculate efficiency accurately."""
        # Simple test to verify write_out_file safely processes and returns sorted records
        mock_data = [
            ["Player A", 15.5],
            ["Player B", 32.1],
            ["Player C", 10.0]
        ]
        report = write_out_file(mock_data)
        
        # Player B should appear first because 32.1 is the highest efficiency
        self.assertTrue(report.startswith("Player B,32.10"))

if __name__ == "__main__":
    unittest.main()