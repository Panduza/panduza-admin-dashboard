#!/bin/bash

# Get system
id=`lsb_release -i`
id=`echo $id | cut -c17-`
ve=`lsb_release -r`
ve=`echo $ve | cut -c10-`
osv=`echo ${id}_${ve}`
echo "OS: [$osv]"

# ===================================================================
# PARAMETERS
python_venv_path=/usr/local/bin/panduza/venv

package_panduza="git+https://github.com/Panduza/panduza-py.git@main#egg=panduza&subdirectory=client/"
package_panduza_platform="git+https://github.com/Panduza/panduza-py.git@main#egg=panduza_platform&subdirectory=platform/"

# package_panduza_admin_dashboard="git+https://github.com/Panduza/panduza-admin-dashboard"
package_panduza_admin_dashboard=/home/xdoctorwhoz/work/panduza-admin-dashboard

service_panduza_admin_path=/etc/systemd/system/panduza-admin.service

# ===================================================================

# 
function install_systemctl_sudo_permissions() {
    echo "%LimitedAdmins ALL=NOPASSWD: /bin/systemctl start panduza-py-platform.service" > /etc/sudoers.d/panduza
}

#
function install_systemctl_admin_service() {
    echo "[Unit]" > $service_panduza_admin_path
    echo "Description=Platform Python to support Panduza Meta Drivers" >> $service_panduza_admin_path
    echo "After=network.target" >> $service_panduza_admin_path
    echo "[Service]" >> $service_panduza_admin_path
    echo "User=root" >> $service_panduza_admin_path
    echo "ExecStart=${python_venv_path}/bin/python3 ${python_venv_path}/lib/python3.10/site-packages/panduza_admin_dashboard/__main__.py" >> $service_panduza_admin_path
    echo "ExecStop=/bin/kill $MAINPID" >> $service_panduza_admin_path
    echo "[Install]" >> $service_panduza_admin_path
    echo "WantedBy=multi-user.target" >> $service_panduza_admin_path
}

# --------------------------
# Ubuntu_22.04
# --------------------------

if [[ $osv == "Ubuntu_22.04" ]]; then
    python3 -m venv ${python_venv_path}
    ${python_venv_path}/bin/pip install numpy
    ${python_venv_path}/bin/pip install nicegui==1.3.1
    ${python_venv_path}/bin/pip install ${package_panduza}
    ${python_venv_path}/bin/pip install ${package_panduza_platform}
    ${python_venv_path}/bin/pip install ${package_panduza_admin_dashboard}
    install_systemctl_admin_service
    install_systemctl_sudo_permissions
    systemctl daemon-reload
    systemctl enable panduza-admin.service
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


