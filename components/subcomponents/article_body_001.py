# components/subcomponents/image_bounded.py

from components.htmlTags import HTMLContaining, HTMLSimple
from components.base import ComponentBase


class ArticleBody001(ComponentBase):
    def __init__(self):
        super().__init__(
            HTMLContaining.DIV,
            self.__class__.__name__,
            ["article_body_001"]
        )
        self.addComponent(
            self,ComponentBase(HTMLContaining.H1, "article_body","article_body",{},
            "Desarrollando Una auténtica relación con Cristo",
        ))