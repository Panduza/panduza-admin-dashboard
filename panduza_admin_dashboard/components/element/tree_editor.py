from nicegui import ui

from utils.tree import TreeFile
from utils.tree import TreeLibrary



class TreeEditor:

    def __init__(self, on_item_dev_selected=None) -> None:

        self.current_tree = None
        self.on_item_dev_selected = on_item_dev_selected

        self.data = [
            {'id': 'section_devices', 'label': 'devices', 'children': []},
            # {'id': 'section_benches', 'label': 'benches', 'children': []},
            # {'id': 'section_brokers', 'label': 'brokers', 'children': []},
        ]

        self.ui_container = ui.element('div')



    # ---

    def delete_tree(self):
        self.current_tree.delete()
        TreeLibrary.GET().notify()

    # ---

    def use_tree(self, name):
        
        self.current_tree = TreeLibrary.GET().get_tree(name=name)

        self.ui_container.clear()
        with self.ui_container:
            with ui.card().tight():
                with ui.element('div').classes('px-4'):
                    # self.ui_title = ui.label()
                    self.ui_title = ui.input(label='Name', 
                        placeholder='device_name',
                        value=str(self.current_tree.name),
                        on_change=self.rename_tree,
                        validation={'Input too long': lambda value: len(value) < 20}).classes("text-xl mt-2")
            
                with ui.element('div').classes('px-4 flex'):
                    ui.button("New Device", on_click=self.create_device).classes("m-2")
                    ui.element('div').classes('grow')
                    # ui.toggle(["on", "off"], value="off", on_change=).classes("m-2")
                    ui.button("Active", on_click=self.activate_tree).classes("m-2")

                with ui.element('div').classes('px-4'):
                    self.ui_tree = ui.tree(self.data, on_select=self.select)

                with ui.element('div').classes('px-4 flex justify-end'):
                    ui.button("Delete", color='red', on_click=self.delete_tree).classes('m-2')

        
        self.update_tree_data()

    # ---

    def rename_tree(self, e):
        """Rename the current tree
        """
        assert self.current_tree

        try:
            self.current_tree.rename(e.value)
        except Exception as e:
            ui.notify(str(e), type='warning')

        TreeLibrary.GET().notify()

    # ---

    def activate_tree(self):
        # Save the tree file and update ui
        if self.current_tree:
            self.current_tree.activate()
        

    def save_tree(self, item = None):
        print("okkkk save !!!")

        # Save the tree file and update ui
        if self.current_tree:
            self.current_tree.save_to_file()
            self.update_tree_data()


    def select(self, e):
        print("edit device", e)

        obj_idx = e.value

        # Clear section
        if obj_idx is None:
            self.on_item_dev_selected(None)

        if obj_idx.startswith("dev_"):
            print("dev !!")

            if self.on_item_dev_selected:
                device = self.current_tree.get_device(obj_idx)
                device.attach(self.save_tree)
                self.on_item_dev_selected(device)
        else:
            self.on_item_dev_selected(None)



    def create_device(self):

        if self.current_tree:
            self.current_tree.create_device()
            self.save_tree()
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
