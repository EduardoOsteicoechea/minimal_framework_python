# pages/home.py

from pages.base import PageBase
from components.header import PageHeader

class Page(PageBase):
    def __init__(self):
        super().__init__()
        self.header = PageHeader().html
        self.set_title("eduardoos")
