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
        id_str = f' id="{self.idsHierarchy.parentId}"' if self.idsHierarchy.parentId else ""
        attr_str = self._generate_attributes(self.attributes)
        is_simple = isinstance(self.tag_type, HTMLSimple)
        if is_simple:
            return f"<{tag}{id_str}{class_str}{attr_str}>"
        else:
            return f"<{tag}{id_str}{class_str}{attr_str}>{self.content}</{tag}>"

    def addComponent(self, parentComponent: 'ComponentBase', component: 'ComponentBase'):
        if component:
            self.css_file_names.extend(component.css_file_names)
            self.js_file_names.extend(component.js_file_names)
            self.subcomponents.append(component)
            component.idsHierarchy.parentId = parentComponent.idsHierarchy.parentId
            self.idsHierarchy.extractSubcomponentIds(component.idsHierarchy)
            for i in self.subcomponents:
              component.idsHierarchy.append_sibling_id(i.id)
            self.content += component.generate()
            self.content += component.log()

    def html(self) -> str:
        """
        Generates the HTML markup for the component.
        """
        return self.generate()
      
    def log(self):
      """
      Returns a human-readable representation of the object
      """
      return f"""
      <br>
      <br>
      <div>
        <p>tag_type: {self.tag_type}</p>
        <p>id: {self.id}</p>
        <p>idsHierarchy: {self.idsHierarchy}</p>
        <p>classes: {self.classes}</p>
        <p>attributes: {self.attributes}</p>
        <p>css_file_names: {self.css_file_names}</p>
        <p>js_file_names: {self.js_file_names}</p>
        <p>subcomponents: {self.subcomponents}</p>
      <div>
      <br>
      <br>
      """

class IdsHierarchy:
    def __init__(
        self,
        Id,
        level1ChildsIds = [],
        level2ChildsIds = [],
        level3ChildsIds = [],
        level4ChildsIds = [],
        level5ChildsIds = [],
        level6ChildsIds = [],
        level7ChildsIds = [],
        ):
        self.parentId = ""
        self.Id = Id
        self.level1ChildsIds = level1ChildsIds if level1ChildsIds is not None else []
        self.level2ChildsIds = level2ChildsIds if level2ChildsIds is not None else []
        self.level3ChildsIds = level3ChildsIds if level3ChildsIds is not None else []
        self.level4ChildsIds = level4ChildsIds if level4ChildsIds is not None else []
        self.level5ChildsIds = level5ChildsIds if level5ChildsIds is not None else []
        self.level6ChildsIds = level6ChildsIds if level6ChildsIds is not None else []
        self.level7ChildsIds = level7ChildsIds if level7ChildsIds is not None else []
        self.level7ChildsIds = level7ChildsIds if level7ChildsIds is not None else []
        self.siblings = []
      
    def append_sibling_id(self, siblings_id: str):
      if siblings_id not in self.siblings:
        self.siblings.append(siblings_id)
      
    def __str__(self):
      """
      Returns a string representation of the IdsHierarchy object,
      listing all its properties.
      """
      return f"""
      <br>
      <br>
      <div>
        <p>ID: {self.Id}</p>
        <p>Parent ID: {self.parentId}</p>
        <p>Siblings IDs: {self.siblings}</p>
        <p>Level 1 Child IDs: {self.level1ChildsIds}</p>
        <p>Level 2 Child IDs: {self.level2ChildsIds}</p>
        <p>Level 3 Child IDs: {self.level3ChildsIds}</p>
        <p>Level 4 Child IDs: {self.level4ChildsIds}</p>
        <p>Level 5 Child IDs: {self.level5ChildsIds}</p>
        <p>Level 6 Child IDs: {self.level6ChildsIds}</p>
        <p>Level 7 Child IDs: {self.level7ChildsIds}</p>
      <div>
      <br>
      """
        
    def extractSubcomponentIds(self, idsHierarchy: 'IdsHierarchy'):
        # Use sets to prevent duplicates
        new_level1_ids = set(self.level1ChildsIds)
        new_level2_ids = set(self.level2ChildsIds)
        new_level3_ids = set(self.level3ChildsIds)
        new_level4_ids = set(self.level4ChildsIds)
        new_level5_ids = set(self.level5ChildsIds)
        new_level6_ids = set(self.level6ChildsIds)
        new_level7_ids = set(self.level7ChildsIds)

        new_level1_ids.add(idsHierarchy.Id)
        new_level2_ids.update(idsHierarchy.level1ChildsIds)
        new_level3_ids.update(idsHierarchy.level2ChildsIds)
        new_level4_ids.update(idsHierarchy.level3ChildsIds)
        new_level5_ids.update(idsHierarchy.level4ChildsIds)
        new_level6_ids.update(idsHierarchy.level5ChildsIds)
        new_level7_ids.update(idsHierarchy.level6ChildsIds)

        self.level1ChildsIds = sorted(list(new_level1_ids))
        self.level2ChildsIds = sorted(list(new_level2_ids))
        self.level3ChildsIds = sorted(list(new_level3_ids))
        self.level4ChildsIds = sorted(list(new_level4_ids))
        self.level5ChildsIds = sorted(list(new_level5_ids))
        self.level6ChildsIds = sorted(list(new_level6_ids))
        self.level7ChildsIds = sorted(list(new_level7_ids))