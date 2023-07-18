import os
import shutil

TREE_LIBRARY_DIR_PATH="/etc/panduza/trees"
TREE_ACTIVE_PATH="/etc/panduza/tree.json"

from .file import TreeFile

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


