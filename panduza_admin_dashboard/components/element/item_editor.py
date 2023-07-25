from nicegui import ui

from utils.tree import TreeFile
from utils.tree import TreeLibrary

from components.element.item_device_editor import ItemDeviceEditor


class ElementItemEditor:

    def __init__(self) -> None:

        self.current_tree = None


        self.container = ui.element('div')



    def load_item_dev(self, item):
        
        self.container.clear()

        if item:
            with self.container:
                ItemDeviceEditor(item)





