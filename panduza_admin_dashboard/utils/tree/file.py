import os
import json
import shutil

TREE_LIBRARY_DIR_PATH="/etc/panduza/trees"
TREE_ACTIVE_PATH="/etc/panduza/tree.json"

from .device import TreeDevice

class TreeFile:

    def __init__(self, name) -> None:

        self.counter_device = 0

        self.name = name
        self.filepath = os.path.join(TREE_LIBRARY_DIR_PATH, f"{name}.json" )
        self.content = ""
        self.devices = []

        self.load_from_file()

    # ---

    def rename(self, new_name):
        """Rename this tree file
        """
        print(new_name)

    # ---

    def set_content(self, content):
        self.content = content

    # ---

    def load_from_content(self):
        """content => obj
        """
        devices = self.content.get('devices')
        # print("looaddd devviii", devices)
        self.devices.clear()
        for dev in devices:
            new_device = self.create_device()
            new_device.from_dict(dev)

    # ---

    def load_from_file(self):
        """file => content
        """
        try:
            with open(self.filepath, 'r') as f:
                self.content = json.load(f)
            self.load_from_content()
        except FileNotFoundError as e:
            self.content = ""
        except json.JSONDecodeError as e:
            self.content = ""

    # ---

    def execute_deletion_requests(self):
        self.devices = [dev for dev in self.devices if not dev.deletion]

    # ---

    def save_to_content(self):
        """obj => content
        """

        self.execute_deletion_requests()

        tmp = { "devices": [] }

        for dev in self.devices:
            tmp["devices"].append( dev.to_dict() )

        self.content = json.dumps(tmp)

    # ---

    def save_to_file(self):
        """content => file
        """
        self.save_to_content()
        with open(self.filepath, "w") as f:
            f.write(self.content)

    # ---

    def activate(self):
        self.save_to_file()
        shutil.copyfile(self.filepath, TREE_ACTIVE_PATH)

    # ---

    def get_devices(self):
        return self.devices

    # ---

    def get_device(self, idx):
        for dev in self.devices:
            if dev.idx == idx:
                return dev
        return None

    # ---

    def create_device(self):
        new_device = TreeDevice(idx=f"dev_{self.counter_device}")
        self.counter_device += 1
        self.devices.append(new_device)
        return new_device


