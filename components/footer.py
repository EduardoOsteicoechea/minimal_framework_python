# components/footer.py

from htmlTags import HTMLContaining, HTMLSimple
from base import ComponentBase

class PageFooter(ComponentBase):
    def __init__(self):
        super.__init__(HTMLContaining.DIV, "This is the footer",["footer"])
        self.css_file_names.extend(["footer"])
        self.js_file_names.extend(["footer"])