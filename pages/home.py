# pages/home.py


from components.assistant.assistant_general_001 import AssitantGeneral001
from pages.base import PageBase


class HomePage(PageBase):
    def __init__(self):
        super().__init__()
        self.set_title("eduardoos")
        self.add_component(AssitantGeneral001())
