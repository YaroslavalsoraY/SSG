from nodes_splitter import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    result_lst = split_nodes_delimiter([node], "`", TextType.CODE)
    result_lst = split_nodes_delimiter(result_lst, "**", TextType.BOLD)
    result_lst = split_nodes_delimiter(result_lst, "*", TextType.ITALIC)
    result_lst = split_nodes_image(result_lst)
    result_lst = split_nodes_link(result_lst)
    return result_lst
