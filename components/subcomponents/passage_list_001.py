# components/subcomponents/image_bounded.py

from components.htmlTags import HTMLContaining, HTMLSimple
from components.base import ComponentBase


class PassageList001(
    ComponentBase,
    ):
    def __init__(
        self,
        items:[]
        ):
        super().__init__(
            HTMLContaining.OL,
            self.__class__.__name__,
            ["passage_list_001"]
        )
        try:
            if items:
                for item in items:
                    self.addComponent(
                        self,ComponentBase(HTMLContaining.LI, "passage_list_001_item","passage_list_001_item",{},
                        item,
                    ))
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
  