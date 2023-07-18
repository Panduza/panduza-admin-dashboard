from nicegui import ui

from utils.trees import TreeFile
from utils.trees import TreeLibrary




class ElementItemEditor:

    def __init__(self) -> None:

        self.current_tree = None

        # self.data = [
        #     {'id': 'device', 'label': 'devices', 'children': []},
        # ]

        # ui.button("New Device", on_click=self.append_device)

        self.container = ui.element('div').classes('m-4')

        # self.ui_title = ui.label("pok")
        # self.ui_tree = ui.tree(self.data, on_select=self.select)

    def set_item(self, item):
        print(item)



