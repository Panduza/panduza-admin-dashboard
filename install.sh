#!/bin/bash

# Get system
id=`lsb_release -i`
id=`echo $id | cut -c17-`
ve=`lsb_release -r`
ve=`echo $ve | cut -c10-`
osv=`echo ${id}_${ve}`
echo "OS: [$osv]"

# PARAMETERS
python_venv_path=/usr/local/bin/panduza/venv

# 
function install_systemctl_sudo_permissions() {
    echo "%LimitedAdmins ALL=NOPASSWD: /bin/systemctl start panduza-py-platform.service" > /etc/sudoers.d/panduza
}

# 
function install_systemctl_admin_service() {

# [Unit]
# Description=Platform Python to support Panduza Meta Drivers
# After=network.target

# [Service]
# User=root
# ExecStart=/usr/bin/python3 /home/xdoctorwhoz/work/panduza-admin-dashboard/__m>
# ExecStop=/bin/kill $MAINPID

# [Install]
# WantedBy=multi-user.target

}



# pip install "git+https://github.com/Panduza/panduza-admin-dashboard"



# --------------------------
# Ubuntu_22.04
# --------------------------

if [[ $osv == "Ubuntu_22.04" ]]; then
    pip install nicegui==1.3.1
    install_systemctl_sudo_permissions
    exit 0
fi

# --------------------------
# Ubuntu generic way... not garanted!
# --------------------------

if [[ $id == "Ubuntu" ]]; then
    echo "Exact version of $id not managed !"
    echo "Do you want to try installation with a generic process ? (y/n)"
    read input
    if [[ $input == "n" ]]; then
        echo "Quitting..."
        exit 1
    fi
    apt-get install -y python3 python3-pip
    pip install nicegui==1.3.1
    install_systemctl_sudo_permissions
    exit 0
fi

# --------------------------
# ManjaroLinux_23.0.0
# --------------------------

if [[ $osv == "ManjaroLinux_23.0.0" ]]; then
    pacman -S python --noconfirm
    pacman -S python-pip --noconfirm
    python3 -m venv ${python_venv_path}
    ${python_venv_path}/bin/pip install nicegui==1.3.1
    install_systemctl_sudo_permissions
    exit 0
fi

# --------------------------
# ManjaroLinux generic way... not garanted!
# --------------------------

if [[ $id == "ManjaroLinux" ]]; then
    echo "Exact version of $id not managed !"
    echo "Do you want to try installation with a generic process ? (y/n)"
    read input
    if [[ $input == "n" ]]; then
        echo "Quitting..."
        exit 1
    fi
    pacman -S python --noconfirm
    pacman -S python-pip --noconfirm
    python3 -m venv ${python_venv_path}
    ${python_venv_path}/bin/pip install nicegui==1.3.1
    install_systemctl_sudo_permissions
    exit 0
fi



echo "OS NOT SUPPORTED"





#         filename="/etc/systemd/system/panduza-py-platform.service"
#         ui_log_area.push(f"Write file: {filename}")
#         os.makedirs(os.path.dirname(filename), exist_ok=True)
#         with open(filename, "w") as f:
#             f.write("""
# [Unit]
# Description=Platform Python to support Panduza Meta Drivers
# After=network.target

# [Service]
# User=root
# ExecStart=/usr/bin/python3 /usr/local/bin/pza-py-platform-run.py

# [Install]
# WantedBy=multi-user.target
#             """)


