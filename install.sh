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



# ===================================================================

# 
function install_systemctl_sudo_permissions() {
    echo "%LimitedAdmins ALL=NOPASSWD: /bin/systemctl start panduza-py-platform.service" > /etc/sudoers.d/panduza
}

#
service_panduza_admin_path=/etc/systemd/system/panduza-admin.service
function install_systemctl_admin_service() {

    path_to_admin_main=`readlink -e ${python_venv_path}/lib/python3*/site-packages/panduza_admin_dashboard/__main__.py`

    echo "[Unit]" > $service_panduza_admin_path
    echo "Description=Platform Python to support Panduza Meta Drivers" >> $service_panduza_admin_path
    echo "After=network.target" >> $service_panduza_admin_path
    echo "[Service]" >> $service_panduza_admin_path
    echo "User=root" >> $service_panduza_admin_path
    echo "ExecStart=${python_venv_path}/bin/python3 ${path_to_admin_main}" >> $service_panduza_admin_path
    echo "ExecStop=/bin/kill $MAINPID" >> $service_panduza_admin_path
    echo "[Install]" >> $service_panduza_admin_path
    echo "WantedBy=multi-user.target" >> $service_panduza_admin_path
}

#
function generic_install() {
    python3 -m venv ${python_venv_path}

    ${python_venv_path}/bin/pip3 install numpy
    ${python_venv_path}/bin/pip3 install nicegui==1.3.1
    ${python_venv_path}/bin/pip3 install aardvark-py==5.40
    ${python_venv_path}/bin/pip3 install colorama==0.4.6
    ${python_venv_path}/bin/pip3 install paho-mqtt==1.6.1
    ${python_venv_path}/bin/pip3 install pyftdi==0.54.0
    ${python_venv_path}/bin/pip3 install pymodbus==3.3.2
    ${python_venv_path}/bin/pip3 install pyserial==3.5
    ${python_venv_path}/bin/pip3 install pyudev==0.24.0
    ${python_venv_path}/bin/pip3 install pyusb==1.2.1
    ${python_venv_path}/bin/pip3 install PyHamcrest==2.0.4

    ${python_venv_path}/bin/pip3 install "git+https://github.com/Panduza/panduza-py.git@main#egg=panduza&subdirectory=client/"
    ${python_venv_path}/bin/pip3 install "git+https://github.com/Panduza/panduza-py.git@main#egg=panduza_platform&subdirectory=platform/"
    # ${python_venv_path}/bin/pip3 install "git+https://github.com/Panduza/panduza-admin-dashboard"
    ${python_venv_path}/bin/pip3 install /home/rodriguez/work/panduza-admin-dashboard

    install_systemctl_admin_service
    install_systemctl_sudo_permissions
    systemctl daemon-reload
    systemctl enable panduza-admin.service
}

# --------------------------
# Ubuntu_22.04
# --------------------------

if [[ $osv == "Ubuntu_22.04" ]]; then
    apt-get install -y python3 python3-pip python3-venv
    generic_install
    exit 0
fi

# --------------------------
# Ubuntu generic way... not garanted!
# --------------------------

if [[ $id == "Ubuntu" ]]; then
    apt-get install -y python3 python3-pip python3-venv
    generic_install
    exit 0
fi

# --------------------------
# ManjaroLinux_23.0.0
# --------------------------

if [[ $osv == "ManjaroLinux_23.0.0" ]]; then
    pacman -S python --noconfirm
    pacman -S python-pip --noconfirm
    generic_install
    exit 0
fi

# --------------------------
# ManjaroLinux generic way... not garanted!
# --------------------------

if [[ $id == "ManjaroLinux" ]]; then
    pacman -S python --noconfirm
    pacman -S python-pip --noconfirm
    generic_install
    exit 0
fi


echo "OS NOT SUPPORTED"

