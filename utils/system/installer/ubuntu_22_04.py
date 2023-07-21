
from utils.system.process import execute_sys_cmd


def install_mosquitto(ui_log_area = None):
    cmd = ['apt', 'install', "mosquitto", "-y"]
    execute_sys_cmd(cmd, ui_log_area)



