import os
import platform
import sys
import unittest
import requests
from parameterized import parameterized
import pytest

# Function to find a file in the system
def find_file(root_folder, filename):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        if filename in filenames:
            return os.path.join(dirpath, filename)
    return None

# Function to download a file
def download_file(url, save_path):
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
    with open(save_path, 'wb') as file:
        file.write(response.content)

# Function to read the content of a file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to clean text
def clean_text(text):
    return text.strip().lower()

# Function to tokenize text
def tokenize(text):
    return text.split()

# Function to count words
def count_words(text):
    tokens = tokenize(text)
    return {word: tokens.count(word) for word in set(tokens)}

# Decorator to skip test based on OS
def require_os(required_os):
    def decorator(test):
        def wrapper(*args, **kwargs):
            current_os = platform.system().lower()
            if current_os != required_os.lower():
                raise unittest.SkipTest(f"Test requires {required_os} OS. Current OS is {current_os}.")
            return test(*args, **kwargs)
        return wrapper
    return decorator

# Decorator to skip test based on Python version
def require_python_version(major, minor):
    def decorator(test):
        def wrapper(*args, **kwargs):
            current_version = sys.version_info
            if current_version.major != major or current_version.minor != minor:
                raise unittest.SkipTest(f"Test requires Python {major}.{minor}. Current version is {current_version.major}.{current_version.minor}.")
            return test(*args, **kwargs)
        return wrapper
    return decorator

class TestTextFunctions(unittest.TestCase):

    root_directory = '/'  # Set to the root directory for searching

    @parameterized.expand([
        ("pg17192.txt",),
        ("pg932.txt",),
        ("pg1063.txt",),
        ("pg10031.txt",),
        ("pg14082.txt",)
    ])
    def test_clean_text(self, filename):
        file_path = find_file(self.root_directory, filename)
        if file_path:
            text = read_file(file_path)
            cleaned = clean_text(text)
            self.assertIsInstance(cleaned, str)
        else:
            self.fail(f"File {filename} not found")

    @parameterized.expand([
        ("pg17192.txt",),
        ("pg932.txt",),
        ("pg1063.txt",),
        ("pg10031.txt",),
        ("pg14082.txt",)
    ])
    def test_tokenize(self, filename):
        file_path = find_file(self.root_directory, filename)
        if file_path:
            text = read_file(file_path)
            tokens = tokenize(text)
            self.assertIsInstance(tokens, list, f"Tokenizer failed on sample text: {text}")
        else:
            self.fail(f"File {filename} not found")

    @parameterized.expand([
        ("pg17192.txt",),
        ("pg932.txt",),
        ("pg1063.txt",),
        ("pg10031.txt",),
        ("pg14082.txt",)
    ])
    def test_count_words(self, filename):
        file_path = find_file(self.root_directory, filename)
        if file_path:
            text = read_file(file_path)
            counts = count_words(text)
            self.assertIsNotNone(counts, f"Tokenizer failed on sample text: {text}")
            self.assertIsInstance(counts, dict, f"Expected dict, but got {type(counts)}")
        else:
            self.fail(f"File {filename} not found")

    @require_os('windows')
    def test_specific_os(self):
        cleaned = clean_text("This is a test.")
        self.assertIsInstance(cleaned, str)

    @require_python_version(3, 9)
    def test_specific_python_version(self):
        cleaned = clean_text("This is a test.")
        self.assertIsInstance(cleaned, str)

    @pytest.mark.integration
    def test_integration_file_processing(self):
        # Integration test: download, clean, tokenize, and count words
        url = 'https://www.gutenberg.org/cache/epub/14082/pg14082.txt'  # Example URL for a text file
        save_path = 'test_integration_file.txt'

        # Download the file
        download_file(url, save_path)

        # Read the content
        text = read_file(save_path)

        # Clean the text
        cleaned_text = clean_text(text)

        # Tokenize the text
        tokens = tokenize(cleaned_text)

        # Count specific words
        word_counts = count_words(cleaned_text)

        # Check word counts for common words
        common_words = ['the', 'and', 'of', 'to', 'a']
        for word in common_words:
            self.assertIn(word, word_counts)
            self.assertIsInstance(word_counts[word], int)

        # Cleanup downloaded file
        os.remove(save_path)

    @pytest.mark.integration
    def test_integration_with_multiple_files(self):
        # Integration test with multiple files
        files = [
            "https://www.gutenberg.org/cache/epub/17192/pg17192.txt",
            "https://www.gutenberg.org/cache/epub/1063/pg1063.txt"
        ]
        word_to_check = 'the'

        # Process each file
        for i, url in enumerate(files):
            save_path = f'test_integration_file_{i}.txt'

            # Download the file
            download_file(url, save_path)

            # Read the content
            text = read_file(save_path)

            # Clean the text
            cleaned_text = clean_text(text)

            # Tokenize the text
            tokens = tokenize(cleaned_text)

            # Count words
            word_counts = count_words(cleaned_text)

            # Check if the common word is in the counts
            self.assertIn(word_to_check, word_counts)
            self.assertIsInstance(word_counts[word_to_check], int)

            # Cleanup downloaded file
            os.remove(save_path)

if __name__ == '__main__':
    unittest.main()
