from nicegui import ui

from .tree_editor import TreeEditor
from .item_editor import ElementItemEditor
from .tree_library import ElementTreeLibrary


class TreeManager:


    def __init__(self) -> None:

        with ui.element('div').classes('flex flex-nowrap w-full'):

            with ui.element('div').classes('flex-1 ml-4 max-w-xs'):
                self.library = ElementTreeLibrary(on_tree_change=self.on_tree_change)

            with ui.element('div').classes('flex-1 mx-4 max-w-lg'):
                self.tree_editor = TreeEditor(on_item_dev_selected=self.on_item_dev_selected)

            with ui.element('div').classes('flex-1 mr-4 max-w-xs'):
                self.item_editor = ElementItemEditor()

    # ---

    def on_tree_change(self, tree_name):
        self.tree_editor.use_tree(tree_name)

    # ---

    def on_item_dev_selected(self, item_dev):
        self.item_editor.load_item_dev(item_dev)

    # ---

    async def store_new_tree(self, e):
        print(f"pok !! {e.name}")

        text = e.content.read().decode('utf-8')
        print(text)

        # filename="/etc/panduza/tree.json"
        # print(f"Write file: {filename}")
        # os.makedirs(os.path.dirname(filename), exist_ok=True)
        # with open(filename, "w") as f:
        #     f.write(text)




    def up(self):
        self.data[0]['children'].append({'id': 'new_dev'})
        self.ui_tree.update()


