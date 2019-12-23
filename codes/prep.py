# This module is for data preparation
import zipfile, urllib.request, shutil



class Prep(object):

    """
    Data fetch, process cache and preparation
    """
    def __init__(self, url, file_name):
        with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
            with zipfile.ZipFile(file_name) as zf:
                zf.extractall()