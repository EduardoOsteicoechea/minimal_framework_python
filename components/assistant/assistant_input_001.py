# components/subcomponents/image_bounded.py

from components.assistant.action_button_001 import ActionButton001
from components.assistant.assistant_input_textarea_001 import AssistantInputTextarea001
from components.base.htmlTags import HTMLContaining
from components.base.base import ComponentBase


class AssistantInput001(ComponentBase):
    def __init__(self):
        super().__init__(
            HTMLContaining.DIV,
            self.__class__.__name__,
            ["assistant_input_001"]
        )
        self.css_file_names.extend(["assistant_input_001"])
        self.js_file_names.extend(["assistant_input_001"])
        self.addComponent(self,AssistantInputTextarea001())
        self.addComponent(self,ActionButton001())
        self.content += self.log()