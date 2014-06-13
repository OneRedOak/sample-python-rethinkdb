import unittest
from rethink import Rethink


class TestSuite(unittest.TestCase):

    def test(self):
        rethink = Rethink()
        rethink.populate()
        things = rethink.count()
        self.failIf(things != 5)


def main():
    unittest.main()

if __name__ == "__main__":
    main()
