# components/subcomponents/image_bounded.py

from components.htmlTags import HTMLContaining, HTMLSimple
from components.base import ComponentBase


class ArticleTitle001(ComponentBase):
    def __init__(self):
        super().__init__(
            HTMLContaining.DIV,
            self.__class__.__name__,
            ["article_title_001"]
        )
        self.addComponent(
            self,ComponentBase(HTMLContaining.H1, "article_title_heading","article_title_heading",{},
            "Una auténtica relación con Cristo.",
        ))    
        self.addComponent(
            self,ComponentBase(HTMLContaining.BUTTON, "reload_article_button","reload_article_button",{},
            "Recargar",
        ))