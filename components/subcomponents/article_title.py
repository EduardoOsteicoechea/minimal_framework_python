# components/subcomponents/image_bounded.py

from components.htmlTags import HTMLContaining, HTMLSimple
from components.base import ComponentBase


class ArticleTitle001(ComponentBase):
    def __init__(self):
        super().__init__(
            HTMLContaining.DIV,
            self.__class__.__name__,
            ["image_bounded"]
        )
        self.css_file_names.extend(["image_bounded"])
        self.js_file_names.extend(["image_bounded"])
        self.addComponent(
            self,ComponentBase(HTMLContaining.P, "article_title_001","article_title_001",{},
            "this is a parag in the article",
        ))