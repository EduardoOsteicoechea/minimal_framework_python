# components/header.py

from .htmlTags import HTMLContaining, HTMLSimple
from .base import ComponentBase
from components.subcomponents.article_title_001 import ArticleTitle001
from components.subcomponents.article_body_001 import ArticleBody001


class PageArticle001(ComponentBase):
    def __init__(self,jsFileName):
        super().__init__(
            HTMLContaining.DIV,
            self.__class__.__name__,
            ["article_001"]
        )
        self.css_file_names.extend(["article_001"])
        self.js_file_names.extend([jsFileName])
        self.addComponent(self,ArticleTitle001())
        self.addComponent(self,ArticleBody001())