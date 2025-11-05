from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag to convert to HTML.")
        elif self.children is None:
            raise ValueError("ParentNode must have children to convert to HTML.")
        else:
            children_html = ""
            for child in self.children:
                children_html += child.to_html()
            return f"<{self.tag}>{children_html}</{self.tag}>"
