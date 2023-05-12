import unittest
import tempfile
import os
from repository import Repo


class TestRepo(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.repo = Repo(self.temp_file.name)

    def tearDown(self):
        os.remove(self.temp_file.name)

    def test_read(self):
        self.repo._read()
        self.assertIn(self.repo.sentence, self.repo.used)

    def test_add(self):
        self.repo._add("This is a new sentence.")
        self.assertIn("This is a new sentence.", self.repo.used)

    def test_sentence(self):
        self.repo.sentence = "This is a new sentence."
        self.assertEqual(self.repo.sentence, "This is a new sentence.")


if __name__ == '__main__':
    unittest.main()
