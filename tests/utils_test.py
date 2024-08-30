import sys
import os

rpath = os.path.abspath(".")
if rpath not in sys.path:
    sys.path.insert(0, rpath)

import unittest
from src.utils import extract_domain, preprocess_text, count_country_mentions


class TestTextProcessingFunctions(unittest.TestCase):
    def test_extract_domain(self):
        # Test cases for extract_domain
        self.assertEqual(extract_domain("https://www.example.com/path"), "example.com")
        self.assertEqual(extract_domain("http://example.com"), "example.com")
        self.assertEqual(
            extract_domain("https://subdomain.example.co.uk"), "subdomain.example.co.uk"
        )
        self.assertEqual(extract_domain("not-a-url"), None)
        self.assertEqual(extract_domain("https://www.example.com"), "example.com")
        self.assertEqual(extract_domain(""), None)
        self.assertEqual(
            extract_domain("http://www.subdomain.example.com/path"),
            "subdomain.example.com",
        )

    def test_count_country_mentions(self):
        # Test cases for count_country_mentions
        countries = ["USA", "Canada", "Germany"]

        text1 = "The USA and Canada have strong economies."
        expected1 = {"USA": 1, "Canada": 1, "Germany": 0}
        self.assertEqual(count_country_mentions(text1, countries), expected1)

        text2 = "Germany and the USA have long histories."
        expected2 = {"USA": 1, "Canada": 0, "Germany": 1}
        self.assertEqual(count_country_mentions(text2, countries), expected2)

        text3 = "Germany is in Europe. The USA is in America."
        expected3 = {"USA": 1, "Canada": 0, "Germany": 1}
        self.assertEqual(count_country_mentions(text3, countries), expected3)

        text4 = None
        expected4 = {"USA": 0, "Canada": 0, "Germany": 0}
        self.assertEqual(count_country_mentions(text4, countries), expected4)

        text5 = "CanadaCanada USAUSA"
        expected5 = {"USA": 0, "Canada": 0, "Germany": 0}
        self.assertEqual(count_country_mentions(text5, countries), expected5)

    def test_preprocess_text(self):
        # Test cases for preprocess_text
        stop_words = {"and", "the", "is"}

        text1 = "The quick brown fox jumps over the lazy dog."
        expected1 = "quick brown fox jumps over lazy dog."
        self.assertEqual(preprocess_text(text1, stop_words), expected1)

        text2 = "This is a test."
        expected2 = "this a test."
        self.assertEqual(preprocess_text(text2, stop_words), expected2)

        text3 = "Stopwords should be removed and text lowercased."
        expected3 = "stopwords should be removed text lowercased."
        self.assertEqual(preprocess_text(text3, stop_words), expected3)

        text4 = "This contains only stopwords."
        expected4 = "this contains only stopwords."
        self.assertEqual(preprocess_text(text4, stop_words), expected4)

        text5 = "  "
        expected5 = ""
        self.assertEqual(preprocess_text(text5, stop_words), expected5)


if __name__ == "__main__":
    unittest.main()
