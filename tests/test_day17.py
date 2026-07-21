import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from day17 import count_lines_and_words


class CountLinesAndWordsTests(unittest.TestCase):
    def test_counts_lines_and_words_in_text_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = os.path.join(tmpdir, "sample.txt")
            with open(file_path, "w", encoding="utf-8") as handle:
                handle.write("Hello world\nThis is a test\n")

            lines, words = count_lines_and_words(file_path)
            self.assertEqual(lines, 2)
            self.assertEqual(words, 6)


if __name__ == "__main__":
    unittest.main()
