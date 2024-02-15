import argparse
import requests
from bs4 import BeautifulSoup


def count_words(input_data, format):
    """
    Counts the total number of words in the given input data based on its format.

    Args:
        input_data (str or list): The input data to count words from.
        format (str): The format of the input data ('text', 'json', or 'html').

    Returns:
        int: The total number of words counted in the input data.
    """
    total_words = 0

    if format == "text":
        words = input_data.split()
        total_words += len(words)
    elif format == "json":
        for string in input_data:
            words = string.split()
            total_words += len(words)
    elif format == "html":
        text = BeautifulSoup(input_data, "html.parser").get_text()
        words = text.split()
        total_words += len(words)

    return total_words


def count_characters(input_data, format):
    """
    Counts the total number of characters in the given input data based on its format.
    Args:
        input_data (str or list): The input data to count characters from.
        format (str): The format of the input data ('text', 'json', or 'html').

    Returns:
        int: The total number of characters counted in the input data.
    """
    total_characters = 0

    if format == "text":
        total_characters += len(input_data)
    elif format == "json":
        for item in input_data:
            total_characters += len(item)
    elif format == "html": 
        total_characters += len(BeautifulSoup(input_data, "html.parser").get_text())

    return total_characters


def get_bacon_ipsum(params=None):
    """
    Retrieves Bacon Ipsum text from the Bacon Ipsum API using the provided parameters.

    Args:
        params (dict, optional): A dictionary containing the parameters for the API request. Defaults to None.

    Returns:
        tuple: A tuple containing the response data, the number of words, and the number of characters in the response.
    """
    url = 'https://baconipsum.com/api/'
    response = requests.get(url, params=params)
    try:
        response.raise_for_status()
        if params['format'] == 'json':
            response_data = response.json()
            no_of_words = count_words(response_data, params['format'])
            no_of_characters = count_characters(response_data, params['format'])
            return response.json(), no_of_words, no_of_characters
        elif params['format'] == 'text' or params['format'] == 'html':
            response_data = response.text
            no_of_words = count_words(response_data, params['format'])
            no_of_characters = count_characters(response_data, params['format'])
            return response.text, no_of_words, no_of_characters
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")
    return None


def main():
    """
    Main entry point for the script. Parses command line arguments and retrieves Bacon Ipsum text.

    This function sets up the argument parser, processes the command line arguments, makes the API request,
    and returns the retrieved Bacon Ipsum text along with word and character counts.

    Returns:
        tuple: A tuple containing the response data, the number of words, and the number of characters in the response.
               Returns None if there was an error during the request.
    """
    parser = argparse.ArgumentParser(description='Retrieve Bacon Ipsum text from the Bacon Ipsum API.')
    parser.add_argument('-t', '--type', default='all-meat', choices=['all-meat', 'meat-and-filler'],
                        help='Type of bacon text to generate (default: all-meat)')
    parser.add_argument('-p', '--paras', type=int, default=5, help='Number of paragraphs to generate (default:  5)')
    parser.add_argument('-l', '--start-with-lorem', choices=['0', '1'], default='1',
                        help='Whether to start with "lorem" text (default:  1)')
    parser.add_argument('-f', '--format', default='json', choices=['json', 'text', 'html'],
                        help='Format of the response (default: json)')
    parser.add_argument('-s', '--sentences', help='Number of sentences (this overrides paragraphs)')

    args = parser.parse_args()

    params = {'type': args.type, 'paras': args.paras, 'start-with-lorem': args.start_with_lorem, 'format': args.format}
    bacon_ipsum = get_bacon_ipsum(params)
    if bacon_ipsum:
        data, no_words, no_characters = bacon_ipsum
        return data, no_words, no_characters
    else:
        return None, None, None


if __name__ == '__main__':
    data, no_words, no_characters = main()
    if data:
        print(f"Data: {data}\nWords: {no_words}\nCharacters: {no_characters}")
    else:
        print("Failed to retrieve Bacon Ipsum data.")
