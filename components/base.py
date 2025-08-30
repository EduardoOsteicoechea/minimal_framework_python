# components/base.py

from .htmlTags import HTMLContaining, HTMLSimple


class ComponentBase:
    def __init__(
        self,
        tag_type: HTMLContaining | HTMLSimple,
        id: str = "",
        classes: list = [],
        attributes: dict = {},
        content: str = "",
    ):
        self.tag_type = tag_type
        self.id = id
        self.idsHierarchy = IdsHierarchy(self.id)
        self.content = content
        self.classes = classes
        self.attributes = attributes
        self.css_file_names = []
        self.js_file_names = []
        self.subcomponents = []
            
    def _generate_classes(self, classes: list | str = "") -> str:
        """Generates a space-separated class attribute string."""
        if isinstance(classes, list):
            return f' class="{" ".join(classes)}"'
        elif isinstance(classes, str) and classes:
            return f' class="{classes}"'
        return ""
            
    def _generate_attributes(self, attributes: dict = {}) -> str:
        """Generates an attribute string from a dictionary."""
        if not attributes:
            return ""
        attr_list = [f'{key}="{value}"' for key, value in attributes.items()]
        return " " + " ".join(attr_list)

    def generate(self) -> str:
        tag = self.tag_type.value
        class_str = self._generate_classes(self.classes)
        id_str = f' id="{self.id}"' if self.id else ""
        attr_str = self._generate_attributes(self.attributes)
        is_simple = isinstance(self.tag_type, HTMLSimple)
        if is_simple:
            return f"<{tag}{id_str}{class_str}{attr_str}>"
        else:
            return f"<{tag}{id_str}{class_str}{attr_str}>{self.content}</{tag}>"

    def addComponent(self, component: 'ComponentBase'):
        if component:
            self.css_file_names.extend(component.css_file_names)
            self.js_file_names.extend(component.js_file_names)
            self.idsHierarchy.extractSubcomponentIds(component.idsHierarchy)
            self.content += component.generate()

    def html(self) -> str:
        """
        Generates the HTML markup for the component.
        """
        return self.generate()

class IdsHierarchy:
    def __init__(
        self,
        parentId,
        level1ChildsIds = [],
        level2ChildsIds = [],
        level3ChildsIds = [],
        level4ChildsIds = [],
        level5ChildsIds = [],
        level6ChildsIds = [],
        level7ChildsIds = [],
        ):
        self.parentId = parentId
        self.level1ChildsIds = level1ChildsIds if level1ChildsIds is not None else []
        self.level2ChildsIds = level2ChildsIds if level2ChildsIds is not None else []
        self.level3ChildsIds = level3ChildsIds if level3ChildsIds is not None else []
        self.level4ChildsIds = level4ChildsIds if level4ChildsIds is not None else []
        self.level5ChildsIds = level5ChildsIds if level5ChildsIds is not None else []
        self.level6ChildsIds = level6ChildsIds if level6ChildsIds is not None else []
        self.level7ChildsIds = level7ChildsIds if level7ChildsIds is not None else []
        
    def extractSubcomponentIds(self, idsHierarchy: 'IdsHierarchy'):
        if idsHierarchy.parentId:
            self.level1ChildsIds.append(idsHierarchy.parentId)
        if idsHierarchy.level1ChildsIds:
            self.level2ChildsIds.extend(idsHierarchy.level1ChildsIds)
        if idsHierarchy.level2ChildsIds:
            self.level3ChildsIds.extend(idsHierarchy.level2ChildsIds)
        if idsHierarchy.level3ChildsIds:
            self.level4ChildsIds.extend(idsHierarchy.level3ChildsIds)
        if idsHierarchy.level4ChildsIds:
            self.level5ChildsIds.extend(idsHierarchy.level4ChildsIds)
        if idsHierarchy.level5ChildsIds:
            self.level6ChildsIds.extend(idsHierarchy.level5ChildsIds)
        if idsHierarchy.level6ChildsIds:
            self.level7ChildsIds.extend(idsHierarchy.level6ChildsIds)