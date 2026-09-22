"""HW1 Question 3 Tests"""

import sys

sys.path.append('.')
from src.q3 import capitalize_words


"""Please write your tests here."""

def normal_case() -> None:
    capitalize_words("hello everybody")

def already_upper() -> None:
    capitalize_words("Hello everybody")

def empty_first_char() -> None:
    capitalize_words(" hello everybody")

def odd_first_char() -> None:
    capitalize_words("@hello everybody")

def odd_first_and_second_char() -> None:
    captalize_words("*@hello everybody")

def empty_string() -> None:
    capitalize_words("")

def no_letters() -> None:
    capitalize_words("19865315836")