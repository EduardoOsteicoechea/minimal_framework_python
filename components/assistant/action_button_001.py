# components/header.py

from components.base.base import ComponentBase
from components.base.htmlTags import HTMLContaining



class ActionButton001(ComponentBase):
    def __init__(self):
        super().__init__(
            HTMLContaining.BUTTON,
            self.__class__.__name__,
            ["action_button_001"],
            {"type":"button"},
            "Send",
            True
        )
        self.css_file_names.extend(["action_button_001"])
        self.js_file_names.extend(["action_button_001"])