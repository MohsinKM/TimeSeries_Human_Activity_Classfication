# This is the main driver

import libs


# =========================
# CONFIGURE
# =========================
cfg = libs.Config()
utils = libs.Utils(cfg.prj_root)
prp = libs.Prep(utils, cfg)
utils.create_dirs()
# =========================

logger = utils.build_logger("Main")
logger.info("Starting the main code")

# =========================
# DATA PREPARATION
# =========================
prp.fetch_data(cfg.data_url, cfg.dl_data_dir, cfg.ex_data_dir)

logger.info("End of code")

