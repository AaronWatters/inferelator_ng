
import unittest, os

from .. import inferelator_R

class TestDreamSimple(unittest.TestCase):

    def test_run(self):
        inferelator_R.run_inferelator_R("dream4_simplified.R")
