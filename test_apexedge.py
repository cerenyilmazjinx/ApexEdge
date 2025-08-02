# test_apexedge.py
"""
Tests for ApexEdge module.
"""

import unittest
from apexedge import ApexEdge

class TestApexEdge(unittest.TestCase):
    """Test cases for ApexEdge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ApexEdge()
        self.assertIsInstance(instance, ApexEdge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ApexEdge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
