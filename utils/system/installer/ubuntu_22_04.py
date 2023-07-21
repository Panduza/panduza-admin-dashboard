
from utils.system.process import execute_sys_cmd


def install_mosquitto(ui_log_area = None):
    cmd = ['pip', 'install', "git+https://github.com/Panduza/panduza-py.git@pico_dio_integration#egg=panduza_platform&subdirectory=platform/", "--no-color"]
    execute_sys_cmd(cmd, ui_log_area)



