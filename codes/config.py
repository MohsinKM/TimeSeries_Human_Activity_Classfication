# This module is for all the configuration
import os


class Config(object):
    """
    Configuration
    """
    data_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00507/wisdm-dataset.zip"

    prj_root = os.getcwd()

    inp_dat_fname = os.path.join(prj_root, "data", "input", "data.zip")

    def __init__(self):
        pass

    def fetch(self):
        pass