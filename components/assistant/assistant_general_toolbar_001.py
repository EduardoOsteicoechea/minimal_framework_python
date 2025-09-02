# components/header.py

from components.base.base import ComponentBase
from components.subcomponents.button.action_button_001 import ActionButton001
from components.assistant.assistant_input_001 import AssistantInput001
from ..base.htmlTags import HTMLContaining



class AssitantToolbar001(ComponentBase):
    def __init__(self):
        super().__init__(
            HTMLContaining.DIV,
            self.__class__.__name__,
            ["assistant_general_toolbar_001"]
        )
        self.css_file_names.extend(["assistant_general_toolbar_001"])
        self.js_file_names.extend(["assistant_general_toolbar_001"])
        self.addComponent(self,TimeBox001())
        self.addComponent(self,LoadImageButton())
        self.addComponent(self,LoadFileButton())
        self.addComponent(self,ClearInputButton())
        self.addComponent(self,SamplePromptButton())
        self.addComponent(self,ActionButton001())