# pages/home.py

from pages.base import PageBase
from components.header import PageHeader
# from components.article_001 import PageArticle001
from components.subcomponents.article_title_001 import ArticleTitle001
from components.subcomponents.article_body_001 import ArticleBody001


class HomePage(PageBase):
    def __init__(self):
        super().__init__()
        self.set_title("eduardoos")
        self.addComponent(PageHeader())
        # self.addComponent(PageArticle001())
        self.css_file_names.extend(["article_001"])
        self.js_file_names.extend(["article_001"])
        self.addComponent(self,ArticleTitle001())
        self.addComponent(self,ArticleBody001())
