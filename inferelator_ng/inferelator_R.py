"""
Utility for invoking R inferelator implementaion.
"""

import os
import shutil
from . import utils

INFERELATOR_R = utils.local_path("..", "Inferelator", "inferelator.R")

def run_inferelator_R(job_name="dream4_simplified.R"):
    root_path = utils.local_path("..", "Inferelator")
    job_path = utils.local_path("..", "Inferelator", "jobs", job_name)
    output_path = utils.local_path("..", "Inferelator", "output")
    shutil.rmtree(output_path)
    os.chdir(root_path)
    return utils.call_subprocess("Rscript", INFERELATOR_R, job_path)
