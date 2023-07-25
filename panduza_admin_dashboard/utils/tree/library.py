import os
import shutil
from .file import TreeFile

TREE_LIBRARY_DIR_PATH="/etc/panduza/trees"
TREE_ACTIVE_PATH="/etc/panduza/tree.json"

class TreeLibrary:

    def get_list():
        """
        """
        # Create path
        isExist = os.path.exists(TREE_LIBRARY_DIR_PATH)
        if not isExist:
            os.makedirs(TREE_LIBRARY_DIR_PATH)

        # Extract list from files
        results = []
        for file in os.listdir(TREE_LIBRARY_DIR_PATH):
            if file.endswith(".json"):
                results.append(file[:-len(".json")])
        
        # Return a sorted list
        results.sort()
        return results

    # ---

    def tree_name_exists(name):
        """Return true if the name already exists among tree files
        """
        existing_trees = TreeLibrary.get_list()
        for t in existing_trees:
            if name == t:
                return True
        return False

    # ---

    def create_new_tree():
        """Create a new tree
        """

        # Get a unique new name
        i = 0
        new_name = f"new_tree_{i}"
        while TreeLibrary.tree_name_exists(new_name):
            i+=1
            new_name = f"new_tree_{i}"

        # Create the file
        new_tree = TreeFile(new_name)
        new_tree.save_to_file()
        return new_tree

