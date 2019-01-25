import unittest
import MarsRover as MR


class MarsRoverObject():
	def __init__(self):
		self.MR = MR

class TestCollision(unittest.TestCase):
	def setUp(self):
		self.args = ["MarsRover.py","test_input/collision_input"]
		self.expected = "1 2 W\n1 3 S"

	def test_collision(self):
		self.assertEqual(MR.main(self.args, 1), self.expected)

class TestBounds(unittest.TestCase):
	def setUp(self):
		self.args = ["MarsRover.py","test_input/bounds_input"]
		self.expected = "0 2 W\n4 5 N"

	def test_bounds(self):
		self.assertEqual(MR.main(self.args, 1), self.expected)

class TestStaggered(unittest.TestCase):
	def setUp(self):
		self.args1 = ["MarsRover.py","test_input/staggered_input_1"]
		self.args2 = ["MarsRover.py","test_input/staggered_input_2"]
		self.expected = "1 3 N\n5 1 E"


	def test_staggered1(self):
		self.assertEqual(MR.main(self.args1, 1), self.expected)

	def test_staggered2(self):
		self.assertEqual(MR.main(self.args2, 1), self.expected)

class TestMismatch(unittest.TestCase):
	def setUp(self):
		self.args1 = ["MarsRover.py","test_input/mismatch_input_1"]
		self.args2 = ["MarsRover.py","test_input/mismatch_input_2"]
		self.expected_outcome_1 = "1 3 N\n5 1 E"
		self.expected_outcome_2 = "1 3 N\n5 1 E\n4 5 N"

	def test_mismatch1(self):
		self.assertEqual(MR.main(self.args1, 1), self.expected_outcome_1)

	def test_mismatch2(self):
		self.assertEqual(MR.main(self.args2, 1), self.expected_outcome_2)