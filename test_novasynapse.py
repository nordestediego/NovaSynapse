# test_novasynapse.py
"""
Tests for NovaSynapse module.
"""

import unittest
from novasynapse import NovaSynapse

class TestNovaSynapse(unittest.TestCase):
    """Test cases for NovaSynapse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NovaSynapse()
        self.assertIsInstance(instance, NovaSynapse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NovaSynapse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
