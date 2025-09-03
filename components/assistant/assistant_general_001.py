# components/header.py

from components.assistant.assistant_input_001 import AssistantInput001
from components.base.base import ComponentBase
from components.base.htmlTags import HTMLContaining


class AssitantGeneral001(ComponentBase):
    def __init__(self):
        super().__init__(
            HTMLContaining.DIV,
            self.__class__.__name__,
            ["assistant_general_001"],{},"",True
        )
        self.css_file_names.extend(["assistant_general_001"])
        self.js_file_names.extend(["assistant_general_001"])
        self.add_component(self,AssistantInput001())