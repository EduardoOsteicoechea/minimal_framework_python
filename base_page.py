class BasePage:
    def __init__(
        self, 
        title="Eduardo Osteicoechea", 
        css: list = [], 
        js: list = [], 
        is_article: bool = False,
        main_data_file_url = "data_file/sample.json",
        main_api_endpoint = "api/"
        ):
        self.title = title
        self.css = css
        self.js = js
        self.is_article = is_article
        self.css_tags = ""
        self.js_tags = ""
        self.article_tag = ""
        self.main_data_file_url = main_data_file_url
        self.main_api_endpoint = main_api_endpoint

    def _generate_css_tags(self):
        if self.css:
            return "".join([f'<link rel="stylesheet" href="{name}.css">' for name in self.css])
        return ""

    def _generate_js_tags(self):
        if self.js:
            return "".join([f'<script src="{name}.js" defer></script>' for name in self.js])
        return ""

    def _generate_article_tag(self):
        if self.is_article:
            return '<article class="page_article"></article>'
        return ""

    def html(self):
        css_tags = self._generate_css_tags()
        js_tags = self._generate_js_tags()
        article_tag = self._generate_article_tag()
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{self.title}</title>
            <link rel="icon" type="image/x-icon" href="images/favicon.ico">
            <link rel="stylesheet" href="global.css">
            <script src="global.js" defer></script>
            {css_tags}
        </head>
        <body>
            <div class="page_asistant"></div>
            <div class="page_modal"></div>
            <div class="skip_to_content"></div>
            <div class="page_header"></div>
            <aside class="first_sidebar"></aside>
            <main class="main">
                {article_tag}
            </main>
            <aside class="second_sidebar"></aside>
            <footer class="page_footer"></footer>
            <div id="page_dataset_attributes" data-main-data-file-url="{self.main_data_file_url}" data-api-endpoint="{self.main_api_endpoint}"></div>
            {js_tags}
        </body>
        </html>        
        """