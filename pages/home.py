# pages/home.py

from page import Page
from components import PageHeader

class HomePage(Page):
  def __init__(self):
    super().__init__()
    self.header = PageHeader().html
    self.title("eduardoos")
  