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

    # facilitating run from examples folder
    path, filename = os.path.split(prj_root)
    if filename == 'examples':
        prj_root = path

    dl_data_dir = os.path.join(prj_root, "data", "input", "data.zip")
    ex_data_dir = os.path.join(prj_root, "data", "input")

    # RAW data
    # phone and watch data directories
    ph_dat_dir = os.path.join(ex_data_dir, "wisdm-dataset", "raw", "phone")
    wch_dat_dir = os.path.join(ex_data_dir, "wisdm-dataset", "raw", "watch")
    # gyro and accelerometer sensors data
    ph_gyro_dat_dir = os.path.join(ph_dat_dir, "gyro")
    ph_accel_dat_dir  = os.path.join(ph_dat_dir, "accel")
    wch_gyro_dat_dir = os.path.join(wch_dat_dir, "gyro")
    wch_accel_dat_dir = os.path.join(wch_dat_dir, "accel")

    # CACHED DATA
    ph_ac_cached = os.path.join(prj_root, "data", "cached", "ph_ac.csv")
    wch_ac_cached = os.path.join(prj_root, "data", "cached", "wch_ac.csv")
    ph_gr_cached = os.path.join(prj_root, "data", "cached", "ph_gr.csv")
    wch_gr_cached = os.path.join(prj_root, "data", "cached", "wch_gr.csv")
    # ==========================================

    txt_data_cols = ['sub_id', 'acc_cd', 'time_stmp', 'acc_x', 'acc_y', 'acc_z']



    def __init__(self):
        pass

    def fetch(self):
        pass