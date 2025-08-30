# components/header.py

from .htmlTags import HTMLContaining, HTMLSimple
from .base import ComponentBase
from components.subcomponents.image_bounded import ImageBounded


class PageHeader(ComponentBase):
    def __init__(self):
        super().__init__(
            HTMLContaining.DIV,
            self.__class__.__name__,
            ["header"]
        )
        self.css_file_names.extend(["header"])
        self.js_file_names.extend(["header"])
        self.addComponent(self,ImageBounded())
        # self.addComponent(self,
        #     ComponentBase(HTMLContaining.P, "header_p","header_p",{},
        #     "this is a parag in the header",
        # ))