""" model unit tests """

import unittest
from Model import Model

class TestModel(unittest.TestCase):

    def setUp(self):
        """Set up a new Model instance for testing."""
        self.model = Model()

    def test_initialization(self):
        """Test the initial state of the model."""
        self.assertEqual(self.model.screen_width, 800)
        self.assertEqual(self.model.screen_height, 600)
        self.assertEqual(self.model.owners, {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 2})
        self.assertEqual(self.model.oliners_count, [10, 0, 0, 0, 0, 10])

    def test_add_oliners(self):
        """Test adding Oliners to owned buildings."""
        updated_counts = self.model.add_oliners()
        self.assertEqual(updated_counts, [11, 0, 0, 0, 0, 11])  # 1 added to each owned building

    def test_send_oliners(self):
        """Test sending Oliners between buildings."""
        self.model.send_oliners(0, 1, 5)  # Send 5 Oliners from building 0 to 1
        self.assertEqual(self.model.oliners_count[0], 5)  # Should have 5 left
        self.assertEqual(self.model.oliners_count[1], 5)  # Building 1 should now have 5 Oliners

    def test_check_negative(self):
        """Test that negative Oliner counts are reset to zero."""
        self.model.oliners_count = [10, 0, 0, 0, 0, 10]
        self.model.oliners_count[0] = -5  # Simulate a negative count
        self.model.check_negative()
        self.assertEqual(self.model.oliners_count[0], 0)  # Should be reset to 0
        self.assertEqual(self.model.owners[0], 0)  # Owner should also be reset

    def test_check_win(self):
        """Test the win condition."""
        self.model.owners = {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 2}
        self.assertEqual(self.model.check_win(), 0)  # No winner
        self.model.owners = {0: 2, 1: 0, 2: 0, 3: 0, 4: 0, 5: 1}
        self.assertEqual(self.model.check_win(), 3)  # Both players have won

if __name__ == '__main__':
    unittest.main()
