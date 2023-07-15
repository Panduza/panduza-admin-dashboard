import subprocess



def execute_sys_cmd(cmd, ui_log_area=None):

    if ui_log_area:
        ui_log_area.push(f"---\n\t$> {cmd}")

    text = ""
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    alive = True
    while alive:
        # Poll the process to check if it has terminated
        poll = process.poll()
        if poll is not None:
            alive = False

        # Read stdout and stderr
        data_available = True
        while data_available:
            output = process.stdout.readline().decode().strip()
            if output:
                text += output
                if ui_log_area:
                    ui_log_area.push(f"\t{output}")
            else:
                data_available = False


        data_available = True
        while data_available:
            error = process.stderr.readline().decode().strip()
            if error:
                text += error
                if ui_log_area:
                    ui_log_area.push(f"\t{error}")
            else:
                data_available = False

    if ui_log_area:
        ui_log_area.push("---")

    return text




def get_service_activation_status():
    """
    """
    cmd = ['systemctl', 'is-active', "panduza-py-platform.service"]
    status = execute_sys_cmd(cmd)
    return status
