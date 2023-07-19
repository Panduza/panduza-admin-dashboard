import os
import shutil


class TreeDevice:

    def __init__(self, idx=None) -> None:
        self.idx = idx
        self.name = "new device"
        self.model = ""
        self.settings = {}
        self._observer_cbs = []

    def attach(self, observer_cb) -> None:
        self._observer_cbs.append(observer_cb)

    def detach(self, observer_cb) -> None:
        self._observer_cbs.remove(observer_cb)

    def notify(self) -> None:
        for cb in self._observer_cbs:
            cb(self)

    def to_dict(self):
        tmp = {
            "name": self.name,
            "model": self.model
        }
        tmp["settings"] = self.settings
        return tmp

    def from_dict(self, dict_obj):
        self.name = dict_obj.get("name", "")
        self.model = dict_obj.get("model", "")
        self.settings = dict_obj.get("settings", {})

