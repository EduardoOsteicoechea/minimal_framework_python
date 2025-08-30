from enum import Enum

class HTMLContaining(Enum):
    """
    Enumeration for HTML tags that typically contain other elements or text.
    """
    DIV = "div"
    A = "a"
    H1 = "h1"
    H2 = "h2"
    H3 = "h3"
    P = "p"
    OL = "ol"
    UL = "ul"
    LI = "li"
    SPAN = "span"
    FORM = "form"
    TABLE = "table"
    TR = "tr"
    TD = "td"
    BUTTON = "button"
    HEADER = "header"
    FOOTER = "footer"
    NAV = "nav"
    SECTION = "section"
    ARTICLE = "article"
    ASIDE = "aside"
    MAIN = "main"


class HTMLSimple(Enum):
    """
    Enumeration for HTML tags that are typically self-closing (void elements).
    """
    BR = "br"
    IMG = "img"
    INPUT = "input"


class HTMLElements:
    def __init__(self, tag_type: HTMLContaining | HTMLSimple):
      self.tag_type = tag_type
        
    def _generate_classes(self, classes: list = []) -> str:
        """Generates a space-separated class attribute string."""
        if classes:
            return f' class="{" ".join(classes)}"'
        return ""

    def _generate_attributes(self, attributes: dict = {}) -> str:
        """Generates an attribute string from a dictionary."""
        if not attributes:
            return ""
        attr_list = [f'{key}="{value}"' for key, value in attributes.items()]
        return " " + " ".join(attr_list)

    def generate(
        self,
        content: str = "", 
        id: str = "", 
        classes: list = [], 
        attributes: dict = {}
    ) -> str:
        tag = self.tag_type.value
        class_str = self._generate_classes(classes)
        id_str = f' id="{id}"' if id else ""
        attr_str = self._generate_attributes(attributes)
        is_simple = isinstance(self.tag_type, HTMLSimple)
        if is_simple:
            return f"<{tag}{id_str}{class_str}{attr_str}>"
        else:
            return f"<{tag}{id_str}{class_str}{attr_str}>{content}</{tag}>"

    def generate_subcomponent(
        self, 
        tag_type: HTMLContaining | HTMLSimple, 
        content: str = "", 
        id: str = "", 
        classes: list = [], 
        attributes: dict = {}
    ) -> str:
        tag = tag_type.value
        class_str = self._generate_classes(classes)
        id_str = f' id="{id}"' if id else ""
        attr_str = self._generate_attributes(attributes)
        is_simple = isinstance(tag_type, HTMLSimple)
        if is_simple:
            return f"<{tag}{id_str}{class_str}{attr_str}>"
        else:
            return f"<{tag}{id_str}{class_str}{attr_str}>{content}</{tag}>"
