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
        mustLog: bool = False
    ):
        print("")
        print(f"Starting instantiation of: {id}")
        self.id = id
        self.tag_type = tag_type
        self.content = content
        self.classes = classes
        self.attributes = attributes
        self.css_file_names = []
        self.js_file_names = []
        self.subcomponents = []
        self.mustLog = mustLog
        self.parentComponent = None
        self.idsHierarchy = IdsHierarchy(
            self.id, [], [], [], [], [], [], [], self.mustLog)

    def __str__(self):
        """
        Returns a string representation of the IdsHierarchy object,
        listing all its properties.
        """
        return f"""{self.id}"""

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

    def update_siblings_list(self, component: 'ComponentBase'):        
        print(f"Updating siblings for: {self.id}")        
        if self.parentComponent and self.parentComponent.subcomponents:            
            for sibling in self.parentComponent.subcomponents:
                sibling.idsHierarchy.siblings = self.idsHierarchy.level1ChildsIds
                # if sibling.id != component.id:
                #     print(f"Appending '{sibling.id}' to '{component.id}'")
                #     component.idsHierarchy.siblings.append(sibling.id)
                #     sibling.idsHierarchy.siblings.append(component.id)

    def generate(self) -> str:
        print(f"Generating HTML for: {self.id}")
        tag = self.tag_type.value
        class_str = self._generate_classes(self.classes)
        id_str = f' id="{self.idsHierarchy.parentId}"' if self.idsHierarchy.parentId else ""
        attr_str = self._generate_attributes(self.attributes)
        is_simple = isinstance(self.tag_type, HTMLSimple)
        if is_simple:
            return f"<{tag}{id_str}{class_str}{attr_str}>"
        else:
            return f"<{tag}{id_str}{class_str}{attr_str}>{self.content}</{tag}>"

    def add_component(self, parentComponent: 'ComponentBase', component: 'ComponentBase'):
        if not component:
            raise Exception("Null component")
        elif not isinstance(component, ComponentBase):
            raise Exception(f"{type(ComponentBase)} instance expected")
        else:
            print("")
            print(f"Adding {component} to {self.id}")
            
            if component.css_file_names:
                self.css_file_names.extend(component.css_file_names)
                print(f"{len(component.css_file_names)} Css files added")
                
            if component.js_file_names:
                self.js_file_names.extend(component.js_file_names)
                print(f"{len(component.js_file_names)} Js files added")
                
            self.subcomponents.append(component)
            print(f"{len(self.subcomponents)} Subcomponents appended")
            
            self.parentComponent = parentComponent
            print(f"Parent component {parentComponent.id} stored")
            
            component.idsHierarchy.parentId = parentComponent.idsHierarchy.parentId
            print(
                f"Obtained parent id: {parentComponent.idsHierarchy.parentId}")
            
            self.update_siblings_list(component)
            print(f"Updated sublings list")
            
            self.idsHierarchy.extract_subcomponent_ids(component.idsHierarchy)
            print(f"Extracted subcomponent id's")
            print(f"{component.idsHierarchy}")
            
            if self.mustLog:
                self.content += component.log()
                print(f"added subcomponent log do content:")
            
            self.content += component.generate()
            print(f"Generated html content")
                
            print("")

    def html(self) -> str:
        """
        Generates the HTML markup for the component.
        """
        return self.generate()

    def log(self):
        """
        Returns a human-readable representation of the object
        """
        if self.mustLog:
            return f"""
            <br>
            <br>
            <div>
                <p>id: {self.id}</p>
                <p>tag_type: {self.tag_type}</p>
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
        else:
            return ""


class IdsHierarchy:
    def __init__(
        self,
        Id,
        level1ChildsIds=[],
        level2ChildsIds=[],
        level3ChildsIds=[],
        level4ChildsIds=[],
        level5ChildsIds=[],
        level6ChildsIds=[],
        level7ChildsIds=[],
        mustLog=False
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
        self.mustLog = mustLog

    def append_sibling_id(self, siblings_id: str):
        if siblings_id not in self.siblings:
            self.siblings.append(siblings_id)

    def __str__(self):
        """
        Returns a string representation of the IdsHierarchy object,
        listing all its properties.
        """
        if self.mustLog:
            return f"""
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
            """

    def extract_subcomponent_ids(self, idsHierarchy: 'IdsHierarchy'):
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
