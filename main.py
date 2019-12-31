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

ph_acc_df = prp.read_n_cache_all_txt_data(cfg.ph_accel_dat_dir,
                                          cfg.ph_ac_cached)  # phone accel data

ph_gyro_df = prp.read_n_cache_all_txt_data(cfg.ph_gyro_dat_dir,
                                          cfg.ph_gr_cached)  # phone gyro data

logger.info("End of code")

