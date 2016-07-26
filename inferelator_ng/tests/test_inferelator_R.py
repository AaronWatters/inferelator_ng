
import unittest, os, glob

from .. import inferelator_R

class TestDreamSimple(unittest.TestCase):

    def test_simplified_run(self, parameters="dream4_simplified.R"):
        "execute: Rscript inferelator.R jobs/dream4_simplified.R"
        output_path = inferelator_R.run_inferelator_R(parameters)
        # check that the output directory was created
        assert os.path.exists(output_path)
        # check that subdirectory exists
        subdirs = glob.glob(os.path.join(output_path, "*"))
        self.assertEqual(len(subdirs), 1, "one subdir only "+repr((output_path, subdirs)))
        subdir = subdirs[0]
        # check for Rdata output files
        for (pattern, count) in [
            ("betas*.RData", 1), 
            ("combined*.RData", 1),
            ("params*.RData", 1)]:
            glob_path = os.path.join(subdir, pattern)
            matches = glob.glob(glob_path)
            self.assertEqual(len(matches), count, 
                "did not find matches " + repr((glob_path, count, matches)))

    @unittest.skipIf(os.environ.has_key("TRAVIS_TESTING"),
                     "Skipping because of failure to install 'corpcor' R package in Travis")
    def test_simplified_with_TFA(self):
        return self.test_simplified_run("dream4_usetfa_simplified.R")
