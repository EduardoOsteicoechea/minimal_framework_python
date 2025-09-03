# components/header.py

from components.base.base import ComponentBase
from components.base.htmlTags import HTMLContaining
from components.subcomponents.article_title_001 import ArticleTitle001
from components.subcomponents.article_body_001 import ArticleBody001


class PageArticle001(ComponentBase):
    def __init__(self,jsFileName):
        super().__init__(
            HTMLContaining.DIV,
            self.__class__.__name__,
            ["article_001"],
            {"data-content-filename":jsFileName}
        )
        self.css_file_names.extend(["article_001"])
        self.js_file_names.extend(["article_001"])
        self.addComponent(self,ArticleTitle001())
        self.addComponent(self,ArticleBody001())