# This module is for data preparation
import os
import glob
import pandas as pd



class Prep(object):

    """
    Data fetch, process cache and preparation
    """

    def __init__(self, utils, cfg):
        self.logger = utils.build_logger("Prep")
        self.utils = utils
        self.cfg = cfg
        pass


    def fetch_data(self, url, dl_dir, ex_dir):
        """
        Downloads data from url, and save it to dl_dir and extract it to ex_dir
        Args:
            url: url to download data from
            dl_dir: directory where to save
            ex_dir: directory to extract zip file

        Returns:None

        """
        # Download
        self.logger.info("Trying to download data..")
        if not os.path.exists(dl_dir):
            self.utils.download_data(url, dl_dir)
        else:
            self.logger.info(f"{dl_dir} already exist")

        # Extract
        self.logger.info("Trying to extract data..")
        if not (os.path.exists(self.cfg.ph_dat_dir) and os.path.exists(
                self.cfg.wch_dat_dir)):
            self.utils.extract_zip_file(ex_dir, dl_dir)
        else:
            self.logger.info(f"Data already extracted")


    def strip_semicolon(mystr):
        return mystr.split(";")[0]


    def read_n_cache_all_txt_data(self, dat_dir, cache_dir):
        """
        Read all txt data and create master data frame
        Args:
            dat_dir:

        Returns: parent_df

        """
        if os.path.exists(cache_dir):
            self.logger.info("Data previously cached prepared and returning")
            parent_df = pd.read_csv(cache_dir)
            return parent_df

        self.logger.info(f"Reading all text files from: {dat_dir}")
        glob_path = os.path.join(dat_dir, "*.txt")
        txt_files = glob.glob(glob_path)
        df_list = []

        for file_nm in txt_files:
            file_path = os.path.join(dat_dir, file_nm)
            df = pd.read_csv(file_path, header=None)
            df.columns = self.cfg.txt_data_cols
            df['acc_z'] = df['acc_z'].str.rstrip(";")
            df_list.append(df)

        # concatenation of all data frames to one
        parent_df = pd.concat(df_list)
        del df_list
        self.logger.info(f"Read all text files from: {dat_dir}")

        # caching
        self.logger.info(f"Caching data to: {cache_dir}")
        parent_df.to_csv(cache_dir, index=False)
        self.logger.info(f"Caching done, written to: {cache_dir}")

        return parent_df