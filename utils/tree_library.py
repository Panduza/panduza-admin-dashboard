import os
import shutil

TREE_LIBRARY_DIR_PATH="/etc/panduza/trees"
TREE_ACTIVE_PATH="/etc/panduza/tree.json"


class TreeLibrary:

        # os.makedirs(os.path.dirname(filename), exist_ok=True)

    def get_list():
        """
        """
        results = []
        for file in os.listdir(TREE_LIBRARY_DIR_PATH):
            if file.endswith(".json"):
                results.append(file[:len(".json")])
        return results


class TreeFile:
    
    def __init__(self, name) -> None:
        self.filepath = os.path.join(TREE_LIBRARY_DIR_PATH, f"{name}.json" )

    def set_content(self, content):
        self.content = content

    def save(self):
        with open(self.filepath, "w") as f:
            f.write(self.content)


    def activate(self):
        self.save()
        shutil.copyfile(self.filepath, TREE_ACTIVE_PATH)

