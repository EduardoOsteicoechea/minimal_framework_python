# components/footer.py

from .htmlTags import HTMLContaining
from .base import ComponentBase


class PageFooter(ComponentBase):
    def __init__(self):
        super().__init__(
            HTMLContaining.DIV,
            self.__class__.__name__, 
            "This is the footer22222222",
            ["footer"]
        )
        self.css_file_names.extend(["footer"])
        self.js_file_names.extend(["footer"])
        self.addComponent(ComponentBase(HTMLContaining.P, "footer_p","this is a parag in the footer","footer_p"))