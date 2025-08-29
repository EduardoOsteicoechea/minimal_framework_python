# pages/base.py

from components.base import ComponentBase

class PageBase:
    _top = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/x-icon" href="static/favicon.ico">
    <link rel="stylesheet" href="static/style.css">
    """
    _body_tag_open = """
    </head>
    <body>
    """
    _bottom = """
    </body>
    </html>
    """

    def __init__(self):
        self.title = ""
        self.css_files = ""
        self.js_top_files = ""
        self.js_bottom_files = ""
        self.modal = ""
        self.assistant = ""
        self.skip_to_content = ""
        self.header = ""
        self.action_message = ""
        self.sidebar = ""
        self.main_content = ""
        self.aside = ""
        self.footer = ""

    def _css_files_markup(self, names_without_extension: list):
        """Generates <link> tags for CSS files."""
        links = [
            f'<link rel="stylesheet" href="static/{name}.css">'
            for name in names_without_extension
        ]
        return "".join(links)

    def _js_files_markup(self, names_without_extension: list, is_module: bool = False):
        """Generates <script> tags for JavaScript files."""
        module_attr = ' type="module"' if is_module else ''
        scripts = [
            f'<script{module_attr} src="{name}.js"></script>'
            for name in names_without_extension
        ]
        return "".join(scripts)

    def set_title(self, name: str):
        self.title = f'<title>{name}</title>'

    def add_css(self, names: list = []):
        if names:
            self.css_files.join(self._css_files_markup(names))

    def add_js_top(self, names: list = [], is_module: bool = False):
        if names:
            self.js_top_files.join(self._js_files_markup(names, is_module))

    def add_js_bottom(self, names: list = [], is_module: bool = False):
        if names:
            self.js_bottom_files.join(self._js_files_markup(names, is_module))

    def set_content_block(self, block_name: str, markup: str, css_files: list = [], js_files: list = []):
        """Sets content and adds associated files for a specific block."""
        if css_files:
            self.add_css(css_files)
        if js_files:
            self.add_js_bottom(js_files)
        setattr(self, block_name, markup)

    def html(self):
        self.add_css()
        self.add_js_top()
        self.add_js_bottom()        
        parts = [
            self._top,
            self.title,
            self.css_files,
            self.js_top_files,
            self._body_tag_open,
            self.modal,
            self.assistant,
            self.skip_to_content,
            self.header,
            self.action_message,
            self.sidebar,
            self.main_content,
            self.aside,
            self.footer,
            self.js_bottom_files,
            self._bottom
        ]        
        return "".join(parts)
    
    def addComponent(self, component: 'ComponentBase'):
        if component:
            self.add_css(component.css_file_names)
            self.add_js_bottom(component.js_file_names)
            # self.idsHierarchy.extractSubcomponentIds(component.idsHierarchy)
            self.main_content += component.content
