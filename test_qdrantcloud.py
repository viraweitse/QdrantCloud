# test_qdrantcloud.py
"""
Tests for QdrantCloud module.
"""

import unittest
from qdrantcloud import QdrantCloud

class TestQdrantCloud(unittest.TestCase):
    """Test cases for QdrantCloud class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = QdrantCloud()
        self.assertIsInstance(instance, QdrantCloud)
        
    def test_run_method(self):
        """Test the run method."""
        instance = QdrantCloud()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
