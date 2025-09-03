# components/subcomponents/image_bounded.py

from components.base.htmlTags import HTMLContaining
from components.base.base import ComponentBase


class AssistantInputTextarea001(ComponentBase):
    def __init__(self):
        super().__init__(
            HTMLContaining.TEXTAREA,
            self.__class__.__name__,
            ["assistant_input_textarea_001"],{},"",True
        )