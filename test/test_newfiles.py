import unittest
import string
from collections import Counter
from parameterized import parameterized
from tokenizer import tokenize
from tokenizer import count_words
from tokenizer import clean_text
import platform
import sys



# Function to read the content of a file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

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

    @parameterized.expand([
        ("pg17192.txt",),
        ("pg932.txt",),
        ("pg1063.txt",),
        ("pg10031.txt",),
        ("pg14082.txt",)
    ])
    def test_clean_text(self, file_path):
        text = read_file(file_path)
        cleaned = clean_text(text)
        assert isinstance(cleaned, str)

    @parameterized.expand([
        ("pg17192.txt",),
        ("pg932.txt",),
        ("pg1063.txt",),
        ("pg10031.txt",),
        ("pg14082.txt",)
    ])
    def test_tokenize(self, file_path):
        text = read_file(file_path)
        assert isinstance(tokenize(text), list), f"Tokenizer failed on sample text: {text}"

    @parameterized.expand([
        ("pg17192.txt",),
        ("pg932.txt",),
        ("pg1063.txt",),
        ("pg10031.txt",),
        ("pg14082.txt",)
    ])
    def test_count_words(self, file_path):
        text = read_file(file_path)
        counts = count_words(text)
        assert None != len(count_words(text)),  f"Tokenizer failed on sample text: {text}"
        assert isinstance(counts, dict), f"should be a dict ,type {type(data)} received instead"

    @require_os('windows')
    def test_specific_os(self):
        # This test will only run on Windows
        cleaned = clean_text("This is a test.")
        assert isinstance(cleaned, str)

    @require_python_version(3, 9)
    def test_specific_python_version(self):
        # This test will only run on Python 3.9
        cleaned = clean_text("This is a test.")
        assert isinstance(cleaned, str)


if __name__ == '__main__':
    unittest.main()
