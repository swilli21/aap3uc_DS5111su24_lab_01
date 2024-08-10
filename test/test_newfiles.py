import os
import platform
import sys
import unittest
from parameterized import parameterized

# Function to find a file in the system
def find_file(root_folder, filename):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        if filename in filenames:
            return os.path.join(dirpath, filename)
    return None

# Function to read the content of a file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to clean text (assuming you have this function defined)
def clean_text(text):
    # Placeholder implementation, replace with your actual clean_text logic
    return text.strip()

# Function to tokenize text (assuming you have this function defined)
def tokenize(text):
    # Placeholder implementation, replace with your actual tokenize logic
    return text.split()

# Function to count words (assuming you have this function defined)
def count_words(text):
    # Placeholder implementation, replace with your actual count_words logic
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

    # Define the root directory where the search should start
    root_directory = '/'  # Change this to the appropriate root directory if needed

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

if __name__ == '__main__':
    unittest.main()
