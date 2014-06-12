import unittest
from mongo import Mongo


class TestSuite(unittest.TestCase):

    def test(self):
        mongo = Mongo()
        mongo.populate()
        things = mongo.count()
        self.failIf(things != 5)


def main():
    unittest.main()

if __name__ == "__main__":
    main()
