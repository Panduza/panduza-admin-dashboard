import os
import shutil


class TreeDevice:
    
    def __init__(self) -> None:
        pass

    def attach(self, observer_cb) -> None:
        print("Subject: Attached an observer.")
        self._observer_cbs.append(observer_cb)

    def detach(self, observer_cb) -> None:
        self._observer_cbs.remove(observer_cb)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for cb in self._observer_cbs:
            cb()


