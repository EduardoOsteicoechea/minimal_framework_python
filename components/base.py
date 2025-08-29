# components/base.py

from htmlTags import HTMLElements, HTMLContaining, HTMLSimple


class ComponentBase:
    def __init__(
        self,
        tag_type: HTMLContaining | HTMLSimple,
        id: str = "",
        content: str = "",
        classes: list = [],
        attributes: dict = {},
    ):
        self._html_generator = HTMLElements()        
        self.tag_type = tag_type
        self.id = id
        self.content = content
        self.classes = classes
        self.attributes = attributes
        self.css_file_names = []
        self.js_file_names = []
        self.subcomponents = []

    def html(self) -> str:
        """
        Generates the HTML markup for the component.
        """
        return self._html_generator.generate(
            tag_type=self.tag_type,
            id=self.id,
            content=self.content,
            classes=self.classes,
            attributes=self.attributes
        )