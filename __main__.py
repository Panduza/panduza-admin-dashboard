from nicegui import app, ui

import components.page_home    as PageHome
import components.page_install as PageInstall
import components.page_control as PageControl


PageHome.create()
PageInstall.create()
PageControl.create()


ui.run( title="Panduza Admin Dashboard",
        storage_secret='THIS_NEEDS_TO_BE_CHANGED')

