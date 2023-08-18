from nicegui import ui
from utils.tree import TreeLibrary


class ElementTreeLibrary:
    """Manage the list of available trees in the system
    """

    def __init__(self, on_tree_change = None) -> None:
        """Constructor
        """
        # Store callback
        self.on_tree_change = on_tree_change

        # Compose layout
        with ui.card().tight():
            # Display icon
            ui.image('images/logo_card.jpg')

            # Buttons
            with ui.element('div').classes("flex"):
                ui.button("NEW TREE", on_click=self.create_new_tree).classes("flex-1 m-2")

            # List of items
            with ui.element('div').classes("flex"):
                self.radio_container = ui.element('div').classes('')

        self.update_tree_list()
        TreeLibrary.GET().attach(self.update_tree_list)

    # ---

    def change_selected_tree(self, e):
        """Triggered when a new tree is selected
        """
        assert self.on_tree_change
        print(f"Select tree {e.value}")
        self.on_tree_change(e.value)

    # ---

    def create_new_tree(self):
        TreeLibrary.GET().create_new_tree()
        self.update_tree_list()

    # ---

    def update_tree_list(self):
        self.radio_container.clear()
        self.trees = TreeLibrary.GET().get_list()
        self.ui_trees_radio = ui.radio(self.trees, on_change=self.change_selected_tree).props('color=green')
        self.ui_trees_radio.move(self.radio_container)

