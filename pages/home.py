# pages/home.py

from page import Page
from components import PageHeader

class Page(Page):
  def __init__(self):
    self.header = PageHeader().html
    self.title("eduardoos")
  