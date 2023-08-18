import os
import json
import shutil

TREE_LIBRARY_DIR_PATH="/etc/panduza/trees"
TREE_ACTIVE_PATH="/etc/panduza/tree.json"

ADMIN_CONFIG_FILE="/etc/panduza/admin.json"


from .device import TreeDevice

class TreeFile:

    def __init__(self, parent_library, name) -> None:
        """Constructor
        """
        self.parent = parent_library

        self.counter_device = 0

        self.name = name
        self.filepath = os.path.join(TREE_LIBRARY_DIR_PATH, f"{name}.json" )
        self.content = ""
        self.devices = []

        self.load_from_file()

        self._observer_cbs = []

    # ---

    def attach(self, observer_cb) -> None:
        self._observer_cbs.append(observer_cb)

    # ---

    def detach(self, observer_cb) -> None:
        self._observer_cbs.remove(observer_cb)

    # ---

    def notify(self) -> None:
        for cb in self._observer_cbs:
            cb(self)
        self.parent.notify()

    # ---

    def delete(self):
        """
        """
        os.remove(self.filepath)

    # ---

    def rename(self, new_name):
        """Rename this tree file
        """
        print(new_name)
        new_filepath = os.path.join(TREE_LIBRARY_DIR_PATH, f"{new_name}.json" )

        if os.path.isfile(new_filepath):
            raise Exception("This name is already used (rename not allowed)")
        else:
            # Rename the file
            os.rename(self.filepath, new_filepath)
            self.name = new_name
            self.filepath = new_filepath

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

        try:
            with open(ADMIN_CONFIG_FILE) as json_file:
                config_data = json.load(json_file)      
        except Exception as e:
            config_data = {}
            pass  
        config_data["active_tree"] = self.name
        with open(ADMIN_CONFIG_FILE, "w") as json_file:
            json.dump(config_data, json_file)

    # ---

    def is_active(self):
        """Active means that this tree is the tree loaded into the platform
        """
        try:
            with open(ADMIN_CONFIG_FILE) as json_file:
                config_data = json.load(json_file)      
        except Exception as e:
            config_data = {}
            pass  
        active_tree_name = config_data.get("active_tree", "")
        return (active_tree_name == self.name)

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


