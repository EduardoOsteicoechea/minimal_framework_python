# pages/home.py


from components.article.article_001 import PageArticle001
from components.assistant.assistant_general_001 import AssitantGeneral001
from components.header.header import PageHeader
from pages.base import PageBase


class HomePage(PageBase):
    def __init__(self):
        super().__init__()
        self.set_title("eduardoos")
        # self.addComponent(PageHeader())
        self.add_component(AssitantGeneral001())
        # self.addComponent(PageArticle001("stairs_free_width"))
