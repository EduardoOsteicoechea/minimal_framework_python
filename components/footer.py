# components/footer.py

from .htmlTags import HTMLContaining
from .base import ComponentBase

class PageFooter(ComponentBase):
    def __init__(self):
        super().__init__(
            HTMLContaining.DIV,
            self.__class__.__name__, 
            "This is the footer",
            ["footer"]
            )
        self.css_file_names.extend(["footer"])
        self.js_file_names.extend(["footer"])
        self.addComponent(PageFooter())