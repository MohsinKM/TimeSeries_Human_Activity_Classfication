# This is for common utilities function
import os


class Utils(object):
    """
    Common utilities
    """
    def __init__(self, proj_root):
        self.proj_root = proj_root
        pass

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

        dirs_to_create = [input_data_dir, output_data_dir, cached_data_dir]
        # Create target Directory if don't exist

        for data_dir in dirs_to_create:
            if not os.path.exists(data_dir):
                try:
                    original_umask = os.umask(0)
                    os.makedirs(dir)
                    os.chmod(dir, 0o0777)
                finally:
                    os.umask(original_umask)
                print("Directory ", data_dir, " Created ")
            else:
                print("Directory ", data_dir, " already exists")