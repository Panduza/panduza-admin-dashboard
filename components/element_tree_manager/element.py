from nicegui import ui

from components.element_tree_editor import ElementTreeEditor
from components.element_tree_library import ElementTreeLibrary
from components.element_item_editor import ElementItemEditor

class ElementTreeManager:


    def __init__(self) -> None:

        with ui.element('div').classes('flex w-full'):

            with ui.element('div').classes('m-4'):
                self.library = ElementTreeLibrary(on_tree_change=self.on_tree_change)

            with ui.element('div').classes('m-4'):
                self.tree_editor = ElementTreeEditor()

            with ui.element('div').classes('m-4'):
                self.item_editor = ElementItemEditor()


    def on_tree_change(self, tree_name):
        self.tree_editor.use_tree(tree_name)


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


