from nicegui import ui
from utils.tree import TreeLibrary


class ElementTreeLibrary:

    def __init__(self, on_tree_change = None) -> None:
        """Constructor
        """
        # Store callback
        self.on_tree_change = on_tree_change

        # Compose layout
        with ui.card().tight():
            ui.image('images/logo_card.jpg')

            # Buttons
            with ui.element('div').classes("flex"):
                ui.button("NEW TREE", on_click=self.create_new_tree).classes("flex-1 m-2")

            # List of items
            with ui.element('div').classes("flex"):
                self.trees = TreeLibrary.get_list()
                with ui.element('div').classes('') as self.radio_container:
                    self.ui_trees_radio = ui.radio(self.trees, on_change=self.change_selected_tree).props('color=green')

    # ---

    def change_selected_tree(self, e):
        if self.on_tree_change:
            self.on_tree_change(e.value)

    # ---

    def create_new_tree(self):
        TreeLibrary.create_new_tree()
        self.radio_container.remove(self.ui_trees_radio)
        self.trees = TreeLibrary.get_list()
        self.ui_trees_radio = ui.radio(self.trees)
        self.ui_trees_radio.move(self.radio_container)
