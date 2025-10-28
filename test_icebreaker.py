#!/usr/bin/env python3
"""
Tests for the Ice Breaker application.
Run with: python test_icebreaker.py
"""

import sys
import unittest
from icebreaker import IceBreaker


class TestIceBreaker(unittest.TestCase):
    """Test cases for the IceBreaker class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.icebreaker = IceBreaker()
    
    def test_has_questions(self):
        """Test that the ice breaker has questions."""
        questions = self.icebreaker.get_all_questions()
        self.assertGreater(len(questions), 0, "Ice breaker should have at least one question")
    
    def test_get_random_question(self):
        """Test getting a random question."""
        question = self.icebreaker.get_random_question()
        self.assertIsInstance(question, str, "Random question should be a string")
        self.assertGreater(len(question), 0, "Random question should not be empty")
        self.assertIn(question, self.icebreaker.get_all_questions(), 
                     "Random question should be from the question list")
    
    def test_get_multiple_questions(self):
        """Test getting multiple random questions."""
        questions = self.icebreaker.get_multiple_questions(5)
        self.assertEqual(len(questions), 5, "Should return 5 questions")
        self.assertEqual(len(questions), len(set(questions)), 
                        "Questions should be unique")
    
    def test_get_multiple_questions_max_limit(self):
        """Test that we can't get more questions than available."""
        all_questions = self.icebreaker.get_all_questions()
        requested_count = len(all_questions) + 10
        questions = self.icebreaker.get_multiple_questions(requested_count)
        self.assertEqual(len(questions), len(all_questions), 
                        "Should return at most all available questions")
    
    def test_get_all_questions(self):
        """Test getting all questions."""
        questions = self.icebreaker.get_all_questions()
        self.assertIsInstance(questions, list, "Should return a list")
        for question in questions:
            self.assertIsInstance(question, str, "Each question should be a string")
            self.assertGreater(len(question), 0, "Each question should not be empty")
    
    def test_questions_are_copied(self):
        """Test that get_all_questions returns a copy, not the original."""
        questions1 = self.icebreaker.get_all_questions()
        questions2 = self.icebreaker.get_all_questions()
        self.assertIsNot(questions1, questions2, 
                        "get_all_questions should return a copy")
        self.assertEqual(questions1, questions2, 
                        "Copies should have the same content")
    
    def test_randomness(self):
        """Test that random selection is actually random (probabilistic test)."""
        # Get 20 random questions and verify we don't always get the same one
        questions = [self.icebreaker.get_random_question() for _ in range(20)]
        unique_questions = set(questions)
        # With 25+ questions and 20 draws, we should get at least 5 different ones
        self.assertGreater(len(unique_questions), 5, 
                          "Random selection should produce variety")


def run_tests():
    """Run all tests and report results."""
    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIceBreaker)
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return exit code based on results
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(run_tests())
