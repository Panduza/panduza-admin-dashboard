from nicegui import ui

from utils.trees import TreeFile
from utils.trees import TreeLibrary



class ElementTreeEditor:

    def __init__(self) -> None:

        self.current_tree = None

        self.data = [
            {'id': 'device', 'label': 'devices', 'children': []},
        ]

        ui.button("New Device", on_click=self.append_device)

        self.ui_title = ui.label()
        self.ui_tree = ui.tree(self.data, on_select=self.select)



    def use_tree(self, name):
        # print("poook ", name)
        # 
        self.current_tree = TreeFile(name=name)
        self.ui_title.text = str(self.current_tree.name)


    def select(self, e):
        print("edit device", e)


    def append_device(self):

        if self.current_tree:
            self.current_tree.append_device()
            self.data[0]['children'].clear()

            self.devices = self.current_tree.get_devices()
            print(">>> ", self.devices)

            for dev in self.devices:
                self.data[0]['children'].append({
                    'id': '0001',
                    'label': "unamed",
                })

            self.ui_tree.update()



