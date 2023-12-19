import unittest

from .gemini import Gemini


class TestCLI(unittest.TestCase):
    def test_multiturn_generate_content(self):
        gemini = Gemini()
        multiturn_generate_content(gemini)
