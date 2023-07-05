import unittest

test_loader = unittest.TestLoader()
test_suite = test_loader.discover(start_dir="tests", pattern="test_*.py")

test_runner = unittest.TextTestRunner()
test_runner.run(test_suite)

