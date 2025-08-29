# pages/home.py

from pages.base import PageBase
from components.header import PageHeader
from components.footer import PageFooter


class HomePage(PageBase):
    def __init__(self):
        super().__init__()
        self.header = PageHeader().html() 
        self.set_title("eduardoos")
