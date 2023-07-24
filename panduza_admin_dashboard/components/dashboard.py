import os

from nicegui import app, ui

import components.page.home    as PageHome
import components.page.control as PageControl

def run_dashboard():

    script_directory = os.path.dirname(__file__)
    app.add_static_files("/images", os.path.join(script_directory, "..", "images"))

    PageHome.create()
    PageControl.create()

    ui.run( title="Panduza Admin Dashboard",
            storage_secret='THIS_NEEDS_TO_BE_CHANGED')
