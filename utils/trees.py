import os
import shutil

TREE_LIBRARY_DIR_PATH="/etc/panduza/trees"
TREE_ACTIVE_PATH="/etc/panduza/tree.json"


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




class TreeLibrary:

    # os.makedirs(os.path.dirname(filename), exist_ok=True)

    def get_list():
        """
        """
        # Create path
        isExist = os.path.exists(TREE_LIBRARY_DIR_PATH)
        if not isExist:
            os.makedirs(TREE_LIBRARY_DIR_PATH)


        results = []
        for file in os.listdir(TREE_LIBRARY_DIR_PATH):
            if file.endswith(".json"):
                results.append(file[:len(".json")])
        return results

    def name_already_exists(name):
        existing_trees = TreeLibrary.get_list()
        for t in existing_trees:
            if name == t:
                return True
        return False


    def create_new_tree():
        """
        """
        
        # Get a unique new name
        i = 0
        new_name = f"new_tree_{i}.json"
        while TreeLibrary.name_already_exists(new_name):
            i+=1
            new_name = f"new_tree_{i}.json"


        new_tree = TreeFile(new_name)
        new_tree.save()
        return new_tree


