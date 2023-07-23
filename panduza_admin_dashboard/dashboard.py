import os

from nicegui import app, ui

import panduza_admin_dashboard.components.page.home    as PageHome
import panduza_admin_dashboard.components.page.install as PageInstall
import panduza_admin_dashboard.components.page_control as PageControl

def run_dashboard():

    script_directory = os.path.dirname(__file__)
    app.add_static_files("/images", os.path.join(script_directory, "images"))

    PageHome.create()
    PageInstall.create()
    PageControl.create()

    ui.run( title="Panduza Admin Dashboard",
            storage_secret='THIS_NEEDS_TO_BE_CHANGED')
