




# panduza
# panduza_platform
# mosquitto
# systemd files



from .process import execute_sys_cmd


def is_panduza_installed():    
    return True

# ---

def get_panduza_version():
    """Get the panduza version installed (if not panduza is not installed)
    """
    # 
    x = 'Version: '
    version = None

    # Start the command
    cmd = ['pip', 'show', "panduza"]
    output = execute_sys_cmd(cmd)

    # Check if the version line exists
    for line in output.splitlines():
        if line.startswith(x):
            version = line[len(x):]

    # 
    return version

# ---

def get_service_activation_status():
    """
    """
    cmd = ['systemctl', 'is-active', "panduza-py-platform.service"]
    status = execute_sys_cmd(cmd)
    return status
