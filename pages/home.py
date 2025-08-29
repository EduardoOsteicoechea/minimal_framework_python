# pages/home.py

from _ import PageBase
from components import PageHeader

class Page(PageBase):
    def __init__(self):
        super().__init__()
        self.header = PageHeader().html
        self.set_title("eduardoos")
