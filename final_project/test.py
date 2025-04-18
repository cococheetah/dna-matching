import unittest
from main import read, longest_consecutive_str, create_list, main

class TestDNAMatching(unittest.TestCase):
    # AI attribution: Used ChatGPT 4o (accessed 2025-04-01) to learn how to write unit tests.
    # Prompt: "How do I create unit tests in Python?"
    # Based on the suggestion, I created these unit tests.
    
    def test_read(self):
        data = read("test.csv")
        lists = [["Names","AGATG","AATG","TAT"], ["Elle","5","2","8"],["Amani","3","7","4"],["Blair","6","1","5"],["Ashley","3","7","1"]]
        self.assertEqual(data, lists)

    def test_longest_consecutive_str(self):
        result = longest_consecutive_str("AATAATTAATTAATTAAATGAATGAATGAATGAATGAATGTATTATCATTAAATGT", "AATG")
        self.assertEqual(result, 6)

    def test_create_list(self):
        database = [["Names", "AGATG", "AATG"], ["Elle", "3", "5"]]
        sequence = "AGATGAGATGAATGAATGAATGAATG"
        result = create_list(database, sequence)
        self.assertEqual(result, [2, 4])

if __name__ == "__main__":
    unittest.main()
