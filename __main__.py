from nicegui import app, ui

import components.page.home    as PageHome
import components.page.install as PageInstall
import components.page_control as PageControl


app.add_static_files("/images", "images")


PageHome.create()
PageInstall.create()
PageControl.create()


ui.run( title="Panduza Admin Dashboard",
        storage_secret='THIS_NEEDS_TO_BE_CHANGED')

