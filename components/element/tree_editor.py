from nicegui import ui

from utils.tree import TreeFile
from utils.tree import TreeLibrary



class TreeEditor:

    def __init__(self, on_item_dev_selected=None) -> None:

        self.current_tree = None
        self.on_item_dev_selected = on_item_dev_selected

        self.data = [
            {'id': 'section_devices', 'label': 'devices', 'children': []},
            {'id': 'section_benches', 'label': 'benches', 'children': []},
            {'id': 'section_brokers', 'label': 'brokers', 'children': []},
        ]

        ui.button("New Device", on_click=self.create_device)

        self.ui_title = ui.label()
        self.ui_tree = ui.tree(self.data, on_select=self.select)


    def use_tree(self, name):
        # print("poook ", name)
        # 
        self.current_tree = TreeFile(name=name)
        self.ui_title.text = str(self.current_tree.name)

        self.update_tree_data()


    def save_tree(self, item):
        print("okkkk save !!!")
        
        if self.current_tree:
            self.current_tree.save_to_file()


    def select(self, e):
        print("edit device", e)

        obj_idx = e.value

        if obj_idx is None:
            return

        if obj_idx.startswith("dev_"):
            print("dev !!")

            if self.on_item_dev_selected:
                device = self.current_tree.get_device(obj_idx)
                device.attach(self.save_tree)
                self.on_item_dev_selected(device)


    def create_device(self):

        if self.current_tree:
            self.current_tree.create_device()

            self.update_tree_data()


    def update_tree_data(self):
        self.devices = self.current_tree.get_devices()

        # Update devices
        self.data[0]['children'].clear()
        for dev in self.devices:
            self.data[0]['children'].append({
                'id': dev.idx,
                'label': dev.name,
            })

        self.ui_tree.update()
