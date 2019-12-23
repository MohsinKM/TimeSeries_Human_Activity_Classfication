# This module is for data preparation
import os
import shutil
import zipfile
import urllib.request



class Prep(object):

    """
    Data fetch, process cache and preparation
    """

    def __init__(self, utils):
        self.logger = utils.build_logger("Prep")
        pass

    def download_data(self, url, file_name):
        """
        Downloading data from the internet.
        Args:
            url: link of the zip file
            file_name: file to be saved

        Returns:
            None
        """

        if not os.path.exists(file_name):
            with urllib.request.urlopen(url) as response, \
                    open(file_name, 'wb') as out_file:
                self.logger.info(f"Downloading data from {url} and saving to "
                                 f"{file_name}")
                shutil.copyfileobj(response, out_file)
                with zipfile.ZipFile(file_name) as zf:
                    zf.extractall()
        else:
            self.logger.info(f"{file_name} already exist")