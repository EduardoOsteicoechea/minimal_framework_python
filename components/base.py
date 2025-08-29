# components/base.py

from .htmlTags import HTMLElements, HTMLContaining, HTMLSimple


class ComponentBase:
    def __init__(
        self,
        tag_type: HTMLContaining | HTMLSimple,
        id: str = "",
        content: str = "",
        classes: list = [],
        attributes: dict = {},
    ):
        self._html_generator = HTMLElements(tag_type)
        self.tag_type = tag_type
        self.id = id
        self.idsHierarchy = IdsHierarchy(self.id)
        self.content = content
        self.classes = classes
        self.attributes = attributes
        self.css_file_names = []
        self.js_file_names = []
        self.subcomponents = []

    def addComponent(self, component: 'ComponentBase'):
        if component:
            self.css_file_names.extend(component.css_file_names)
            self.js_file_names.extend(component.js_file_names)
            self.idsHierarchy.extractSubcomponentIds(component.idsHierarchy)

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