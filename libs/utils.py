# This is for common utilities function
import os
import sys
import logging


class Utils(object):
    """
    Common utilities
    """
    def __init__(self, proj_root):
        self.proj_root = proj_root
        pass

    @staticmethod
    def build_logger(name):
        """
        This method creates a logger for the caller module. Example:
        logger = build_logger("main")
        now logger.info("Print something") will print
        Args:
            name: caller module name, a string

        Returns:
            a logger object.

        """
        formatter = logging.Formatter(
            fmt='%(asctime)s %(name)s %(levelname)s>  %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S')
        handler = logging.FileHandler('log/' + name + '.log', mode='w')
        handler.setFormatter(formatter)
        screen_handler = logging.StreamHandler(stream=sys.stdout)
        screen_handler.setFormatter(formatter)
        _logger = logging.getLogger(name)
        _logger.setLevel(logging.INFO)
        _logger.addHandler(handler)
        _logger.addHandler(screen_handler)
        return _logger

    @staticmethod
    def change_file_permissions_recursive(path, mode):
        """
        This method is to change permission of files and directories.
        Args:
            path: directory or file path
            mode: permission mode in octal. E.g. 0o0777

        Returns:
            None
        """
        for rt, dirs, files in os.walk(path, topdown=False):
            for dr in [os.path.join(rt, d) for d in dirs]:
                os.chmod(dr, mode)
                print(f"{os} permission changed to {mode}")
        for file in [os.path.join(rt, f) for f in files]:
            os.chmod(file, mode)
            print(f"{os} permission changed to {mode}")

    def create_dirs(self):
        """
        Create necessary folder structures, data/input, data/output, data/cached
        Args: None
        Returns: None
        """
        assert os.path.exists(self.proj_root), "Provide project path:"

        input_data_dir = os.path.join(self.proj_root, "data", "input")
        output_data_dir = os.path.join(self.proj_root, "data", "output")
        cached_data_dir = os.path.join(self.proj_root, "data", "cached")
        log_data_dir = os.path.join(self.proj_root, "log")

        dirs_to_create = [input_data_dir, output_data_dir, cached_data_dir,
                          log_data_dir]
        # Create target Directory if don't exist

        for data_dir in dirs_to_create:
            if not os.path.exists(data_dir):
                os.makedirs(data_dir)
                self.change_file_permissions_recursive(data_dir, 0o777)
                print("Directory ", data_dir, " Created ")
            else:
                print("Directory ", data_dir, " already exists")