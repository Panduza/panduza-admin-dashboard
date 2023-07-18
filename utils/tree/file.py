import os
import shutil

TREE_LIBRARY_DIR_PATH="/etc/panduza/trees"
TREE_ACTIVE_PATH="/etc/panduza/tree.json"

class TreeFile:

    def __init__(self, name) -> None:

        self.counter_device = 0

        self.name = name
        self.filepath = os.path.join(TREE_LIBRARY_DIR_PATH, f"{name}.json" )
        self.content = ""
        self.obj = { "devices": [] }

    def set_content(self, content):
        self.content = content

    def load_from_file(self):
        pass

    def load_from_content(self):
        pass

    def save(self):
        with open(self.filepath, "w") as f:
            f.write(self.content)

    def activate(self):
        self.save()
        shutil.copyfile(self.filepath, TREE_ACTIVE_PATH)

    def get_devices(self):
        return self.obj["devices"]

    def get_device(self, idx):
        for dev in self.obj["devices"]:
            if dev["idx"] == idx:
                return dev
        return None

    def append_device(self):
        new_device = {
            "idx": f"dev_{self.counter_device}",
            "name": "new device",
            "model": ""
        }
        self.obj["devices"].append(new_device)



