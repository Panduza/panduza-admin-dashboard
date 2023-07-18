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




class TreeLibrary:

    # os.makedirs(os.path.dirname(filename), exist_ok=True)

    def get_list():
        """
        """
        # Create path
        isExist = os.path.exists(TREE_LIBRARY_DIR_PATH)
        if not isExist:
            os.makedirs(TREE_LIBRARY_DIR_PATH)

        # 
        results = []
        for file in os.listdir(TREE_LIBRARY_DIR_PATH):
            print("!!!!", file)
            if file.endswith(".json"):
                results.append(file[:-len(".json")])
        return results

    # ---

    def tree_name_exists(name):
        existing_trees = TreeLibrary.get_list()
        for t in existing_trees:
            if name == t:
                return True
        return False

    # ---

    def create_new_tree():
        """
        """
        
        # Get a unique new name
        i = 0
        new_name = f"new_tree_{i}"
        while TreeLibrary.tree_name_exists(new_name):
            i+=1
            new_name = f"new_tree_{i}"

        print(">>> ", new_name)


        new_tree = TreeFile(new_name)
        new_tree.save()
        return new_tree


