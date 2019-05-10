class StyleParser:
    def __init__(self, style_text=None):
        self.styles = {}
        if style_text is not None:
            self.parse(style_text)

    def parse(self, style_text):
        style_list = style_text.split(';')
        for item in style_list:
            column_idx = item.find(':')
            style_name = item[:column_idx].strip()
            style_value = item[column_idx+1:].strip()
            self.styles[style_name] = style_value

    def get_style_value(self, style_name):
        if style_name in self.styles:
            return self.styles[style_name]
        else:
            return None

    def __str__(self):
        return 'Styles: ' + str(self.styles)