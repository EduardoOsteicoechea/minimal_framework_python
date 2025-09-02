# components/footer.py

from ..base.htmlTags import HTMLContaining
from ..base.base import ComponentBase


class PageFooter(ComponentBase):
    def __init__(self):
        super().__init__(
            HTMLContaining.DIV,
            self.__class__.__name__,
            ["footer"]
        )
        self.css_file_names.extend(["footer"])
        self.js_file_names.extend(["footer"])
        self.addComponent(
            self,ComponentBase(HTMLContaining.P, "footer_p","footer_p",{},
            "this is a parag in the footer",
        ))