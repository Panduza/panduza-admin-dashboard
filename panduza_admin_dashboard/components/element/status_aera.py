import json
from nicegui import ui


STATUS_FILE_PATH="/etc/panduza/log/status.json"


class StatusAera:

    def __init__(self) -> None:
        self.update_content()


    def update_content(self):

        try:
            # Open the JSON file
            with open(STATUS_FILE_PATH) as json_file:
                # Load the JSON data into a Python object
                data = json.load(json_file)

        
            if data["final_state"] == "initialization":
                ui.label('Error During Initialization').classes("text-white bg-red-600")
                ui.label(data["error_string"])


            print(data)

        except Exception as e:
            # print("!!!!!", e)
            pass


