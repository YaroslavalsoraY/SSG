import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        htmlnode1 = HTMLNode("<a>", "salam", props={"href": "example.com", "target": "_blank"})
        str_node =  'href="example.com" target="_blank"'
        self.assertEqual(htmlnode1.props_to_html(), str_node)

    def test_eq_htmlnode(self):
        htmlnode1 = HTMLNode("<tag>", "value", props={"href": "www.example.com"})
        htmlnode2 = HTMLNode("<tag>", "value", props={"href": "www.example.com"})
        self.assertEqual(htmlnode1.tag, htmlnode2.tag)
    
    def test_not_eq_htmlnode(self):
        htmlnode1 = HTMLNode("<tag>", "value", props={"href": "www.example.com"})
        htmlnode2 = HTMLNode("<tag>", "value", props={"href": "www.example.com"})
        self.assertNotEqual(htmlnode1.tag, htmlnode2.value)


class TestLeafNode(unittest.TestCase):
    def test_to_html_leaf(self):
        leafnode1 = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})
        result_str = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(leafnode1.to_html(), result_str)
    
    def test_to_html_leaf_no_props(self):
        leafnode1 = LeafNode("p", "This is a paragraph of text.")
        result_str = "<p>This is a paragraph of text.</p>"
        self.assertEqual(leafnode1.to_html(), result_str)

    def test_to_html_leaf_no_tag(self):
        leafnode1 = LeafNode(value="Some text")
        result_str = "Some text"
        self.assertEqual(leafnode1.to_html(), result_str)


class TestParentNode(unittest.TestCase):
    def test_base_functions(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        result_str = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), result_str)
    
    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
    

if __name__ == "__main__":
    unittest.main()
