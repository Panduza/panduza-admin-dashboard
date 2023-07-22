#!/bin/bash

id=`lsb_release -i`
id=`echo $id | cut -c17-`

ve=`lsb_release -r`
ve=`echo $ve | cut -c10-`

osv=`echo ${id}_${ve}`

echo "OS: [$osv]"

# --------------------------
# Ubuntu_22.04
# --------------------------

if [[ $osv == "Ubuntu_22.04" ]]; then

pip install nicegui==1.3.1

echo "%LimitedAdmins ALL=NOPASSWD: /bin/systemctl start panduza-py-platform.service" > /etc/sudoers.d/panduza

fi






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


