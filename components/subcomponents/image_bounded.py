# components/subcomponents/image_bounded.py

from components.htmlTags import HTMLContaining, HTMLSimple
from components.base import ComponentBase


class ImageBounded(ComponentBase):
    def __init__(self):
        super().__init__(
            HTMLContaining.DIV,
            self.__class__.__name__,
            ["image_bounded"]
        )
        self.css_file_names.extend(["image_bounded"])
        self.js_file_names.extend(["image_bounded"])
        self.addComponent(self,
            ComponentBase(HTMLSimple.IMG, "personal_photo","header_personal_photo",{
                #"src":"static/images/personal_photo_white_head_600x600.jpg", 
                "width":"300%",
                "alt":"",
                "style":"right:55px;top:0px"
            },
            "this is a parag in the header",
        ))