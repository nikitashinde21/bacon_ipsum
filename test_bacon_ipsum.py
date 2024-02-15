import unittest
import requests
from unittest.mock import patch, MagicMock
from bacon_ipsum import count_words, count_characters, get_bacon_ipsum


class TestBaconIpsumScript(unittest.TestCase):

    @patch('requests.get')
    def test_count_words(self, mock_get):
        """
        Test case to verify the count_words function.
        """
        mock_get.return_value.__enter__.return_value.json.return_value = [
            "Hello world",
            "This is a test sentence."
        ]

        # Call the function with mocked data
        words = count_words(["Hello world", "This is a test sentence."], 'json')

        # Assert the expected output
        self.assertEqual(words, 7)

    @patch('requests.get')
    def test_count_characters(self, mock_get):
        """
        Test case to verify the count_characters function.
        """
        mock_get.return_value.__enter__.return_value.text.return_value = "Hello world"

        # Call the function with mocked data
        characters_when_text = count_characters("Hello world", 'text')
        characters_when_json = count_characters(["Hello world!"], 'json')
        characters_when_html = count_characters("Hello world. How are you", 'html')

        # Assert the expected output
        self.assertEqual(characters_when_text, 11)
        self.assertEqual(characters_when_json, 12)
        self.assertEqual(characters_when_html, 24)

    @patch('requests.get')
    def test_get_bacon_ipsum_raises_http_error(self, mock_get):
        """
        Test case to verify that get_bacon_ipsum function raises HTTPError
        """
        mock_get.side_effect = requests.exceptions.HTTPError("HTTP Error")

        # Use assertRaises to check that the function raises the expected exception
        with self.assertRaises(requests.exceptions.HTTPError):
            get_bacon_ipsum({'format': 'json'})

    @patch('requests.get')
    def test_get_bacon_ipsum_returns_expected_values(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = [
            "Hello world",
            "This is a test sentence."
        ]
        mock_get.return_value = mock_response

        # Call the function with mocked data
        data, words, characters = get_bacon_ipsum({'format': 'json'})

        # Assert the expected output
        self.assertEqual(data, ["Hello world", "This is a test sentence."])
        self.assertEqual(words, 7)
        self.assertEqual(characters, 35)


# Run the tests
if __name__ == '__main__':
    unittest.main()
