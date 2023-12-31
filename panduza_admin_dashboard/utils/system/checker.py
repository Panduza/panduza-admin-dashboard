




# panduza
# panduza_platform
# mosquitto
# systemd files



from .process import execute_sys_cmd


def is_panduza_installed():
    return True

# ---

CACHE_OSV = None
def get_osv(ui_log_area = None):
    """
    """
    # Use cache if exists
    global CACHE_OSV
    if CACHE_OSV:
        return CACHE_OSV

    # 
    osv = None
    os = None
    version = None

    # Logs
    if ui_log_area:
        ui_log_area.push("Check Distribution")

    # Check distribution
    cmd = ["lsb_release", "-i"]
    text = execute_sys_cmd(cmd, ui_log_area)
    if text.startswith("Distributor ID:"):
        os = text[len("Distributor ID:\t"):]
        if ui_log_area:
            ui_log_area.push(os)

    # Logs
    if ui_log_area:
        ui_log_area.push("Check Release")

    # Check os
    cmd = ["lsb_release", "-r"]
    text = execute_sys_cmd(cmd, ui_log_area)
    if text.startswith("Release:"):
        version = text[len("Release:\t"):]

        if ui_log_area:
            ui_log_area.push(version)

    # 
    osv = f'{os.rstrip()}_{version.rstrip()}'
    if ui_log_area:
        ui_log_area.push(osv)

    # Set cache and return
    CACHE_OSV = osv
    return osv

# ---

def get_pip_module_version(module_name):
    """Get the panduza version installed (if not panduza is not installed)
    """
    # Init
    x = 'Version: '
    version = None

    # Start the command
    cmd = ['pip', 'show', module_name]
    output = execute_sys_cmd(cmd)

    # Check if the version line exists
    for line in output.splitlines():
        if line.startswith(x):
            version = line[len(x):]

    # Return
    return version

# ---

def get_panduza_version():
    return get_pip_module_version('panduza')

# ---

def get_panduza_platform_version():
    return get_pip_module_version('panduza-platform')

# ---

def get_service_activation_status():
    """
    """
    cmd = ['systemctl', 'is-active', "panduza-py-platform.service"]
    status = execute_sys_cmd(cmd)
    return status.strip()

# ---

def get_service_mosquitto_activation_status():
    """
    """
    cmd = ['systemctl', 'is-active', "mosquitto.service"]
    status = execute_sys_cmd(cmd)
    return status.strip()


# ---

def get_service_mosquitto_version():
    """
    """
    # Init
    x = 'mosquitto version '
    version = None

    cmd = ['mosquitto', '-h']
    output = execute_sys_cmd(cmd)

    # Check if the version line exists
    for line in output.splitlines():
        if line.startswith(x):
            version = line[len(x):]

    return version

