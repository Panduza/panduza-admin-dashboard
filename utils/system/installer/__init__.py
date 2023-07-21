import utils.system.installer.ubuntu_22_04 as ubuntu_22_04




def install_mosquitto(osv, ui_log_area=None):
    """Install Mosquitto Broker
    """
    if osv == "ubuntu_22_04":
        ubuntu_22_04.install_mosquitto(ui_log_area)
    else:
        raise Exception(f"{osv} not supported")


