# This module is for all the configuration
import os


class Config(object):
    """
    Configuration
    """
    data_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/" \
               "00507/wisdm-dataset.zip"

    # ==========================================
    # PATH VARIABLES
    # ==========================================
    prj_root = os.getcwd()
    dl_data_dir = os.path.join(prj_root, "data", "input", "data.zip")
    ex_data_dir = os.path.join(prj_root, "data", "input")

    # phone and watch data directories
    ph_dat_dir = os.path.join(ex_data_dir, "wisdm-dataset", "raw", "phone")
    wch_dat_dir = os.path.join(ex_data_dir, "wisdm-dataset", "raw", "watch")
    # gyro and accelerometer sensors data
    ph_gyro_dat_dir = os.path.join(ph_dat_dir, "gyro")
    ph_accel_dat_dir  = os.path.join(ph_dat_dir, "accel")
    wch_gyro_dat_dir = os.path.join(wch_dat_dir, "gyro")
    wch_accel_dat_dir = os.path.join(wch_dat_dir, "accel")
    # ==========================================


    def __init__(self):
        pass

    def fetch(self):
        pass