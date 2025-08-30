# components/header.py

from .htmlTags import HTMLContaining
from .base import ComponentBase


class PageHeader(ComponentBase):
    def __init__(self):
        super().__init__(
            HTMLContaining.DIV,
            self.__class__.__name__,
            ["header"]
        )
        self.css_file_names.extend(["header"])
        self.js_file_names.extend(["header"])
        self.addComponent(
            ComponentBase(HTMLContaining.P, "header_p","header_p",{},
            "this is a parag in the header",
        ))