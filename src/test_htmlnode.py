import unittest

from htmlnode import HTMLNode


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

if __name__ == "__main__":
    unittest.main()
