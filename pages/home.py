# pages/home.py

from pages.base import PageBase
from components.header import PageHeader
from components.article_001 import PageArticle001


class HomePage(PageBase):
    def __init__(self):
        super().__init__()
        self.set_title("eduardoos")
        self.addComponent(PageHeader())
        self.addComponent(PageArticle001())
