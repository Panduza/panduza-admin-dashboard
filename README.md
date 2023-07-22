# panduza-admin-dashboard



sudo apt-get install libsystemd0
sudo apt-get install libsystemd-dev


sudo visudo -f /etc/sudoers.d/panduza


%LimitedAdmins ALL=NOPASSWD: /bin/systemctl start panduza-py-platform.service


```bash
wget -O - https://raw.githubusercontent.com/Panduza/panduza-admin-dashboard/main/install.sh | sudo bash
```
