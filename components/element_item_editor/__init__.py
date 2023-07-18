from nicegui import ui

from utils.tree import TreeFile
from utils.tree import TreeLibrary

from components.element_item_device_editor import ElementItemDeviceEditor


class ElementItemEditor:

    def __init__(self) -> None:

        self.current_tree = None

        # self.data = [
        #     {'id': 'device', 'label': 'devices', 'children': []},
        # ]

        # ui.button("New Device", on_click=self.append_device)

        self.container = ui.element('div').classes('m-4')

        # self.ui_tree = ui.tree(self.data, on_select=self.select)


    def load_item_dev(self, item):
        print(item)
        self.ui_title = ui.label(str(item))
        self.ui_title.move(self.container)

        with self.container:
            ElementItemDeviceEditor(item)





