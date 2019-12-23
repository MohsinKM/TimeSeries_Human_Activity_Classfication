# This module is for data preparation
import os



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