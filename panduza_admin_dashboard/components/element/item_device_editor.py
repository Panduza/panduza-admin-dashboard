from nicegui import ui

from utils.tree import TreeFile
from utils.tree import TreeLibrary



ref_database = {
    "Hanmatek.Hm310t": {
        "img": "hm310t.jpg",
        "settings": {}
    },
    "Panduza.FakeBpc": {
        "img": "fake_psu.jpg",
        "settings": [
            {
                'name': 'number_of_channel',
                'type': 'int'
            }
        ]
    },
    "Panduza.FakeDioController": {
        "img": "fake_dio.jpg",
        "settings": [
            {
                'name': 'number_of_dio',
                'type': 'int'
            }
        ]
    }
}



class ItemDeviceEditor:

    def __init__(self, item) -> None:
        self.item = item

        with ui.element('div'):
            with ui.card().tight():
                self.ui_image = ui.image('images/none.jpg')
                with ui.element('div').classes('p-4'):
                    ui.input(label='Name', 
                                placeholder='device_name',
                                value=self.item.name,
                                on_change=self.change_name,
                                validation={'Input too long': lambda value: len(value) < 20})

                    choices = list(ref_database.keys())
                    ui.select(choices, value=self.item.ref, on_change=self.change_model)

                    self.ui_settings_container = ui.element('div')

                    ui.button("delete", color='red', on_click=self.delete_item).classes('mt-2')


        self.update_model_specifics()

    # ---

    def delete_item(self):
        self.item.flag_for_deletion()
        self.item.notify()

    # ---

    def change_name(self, e):
        self.item.name = e.value
        self.item.notify()

    # ---

    def change_model(self, e):
        # print(e.value)
        self.item.ref = e.value
        self.item.notify()

        self.update_model_specifics()

    # ---

    def change_setting(self, name, value):
        # print("change ", name, " ", value)
        self.item.settings[name] = value
        self.item.notify()

    # ---

    def update_model_specifics(self):

        params = ref_database.get(self.item.ref, None)
        if params:
            self.ui_image.source = f'images/{params["img"]}'
            # print(self.ui_image.source)
            self.ui_image.update()

            self.ui_settings_container.clear()

            with self.ui_settings_container:

                ui.label("Settings").classes("text-xl mt-2")

                for setting in params["settings"]:

                    if setting['type'] == 'int':
                        default_value = self.item.settings.get(setting['name'], 1)
                        ui.number(label=setting['name'], value=default_value, format='%d',
                            on_change=lambda e: self.change_setting(setting['name'], e.value))


        else:
            self.ui_image.source = 'images/none.jpg'
            self.ui_image.update()

