class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Error")
    
    def props_to_html(self):
        if self.props != None:
            props_str = ""
            for k, v in self.props.items():
                props_str += f'{k}="{v}" '
            return props_str.rstrip()
        
    
    def __repr__(self):
        return f"tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props_to_html()}"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        self.tag = tag
        self.value = value
        self.props = props
    
    def to_html(self):
        if self.value == None:
            raise ValueError("VallueError")
        if self.tag == None:
            return self.value
        if self.props != None:    
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>" 
        return f"<{self.tag}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children: HTMLNode, props=None):
        self.tag = tag
        self.children = children
        self.props = props
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Error")
        if not self.children:
            raise ValueError("Children Error!")
        html_str = ""
        for node in self.children:
            html_str += node.to_html()
        return f"<{self.tag}>" + html_str + f"</{self.tag}>"
