from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_image(old_nodes: list):
    new_nodes = []
    for node in old_nodes:
        temp_lst = extract_markdown_images(node.text)
        if len(temp_lst) == 0 and node.text != "":
            new_nodes.append(node)
            continue
        text = node.text
        for i in range(len(temp_lst)):
            sections = text.split(f"![{temp_lst[i][0]}]({temp_lst[i][1]})", 1)
            if sections[0] != "":   
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(temp_lst[i][0], TextType.IMAGE, temp_lst[i][1]))
            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes: list):
    new_nodes = []
    for node in old_nodes:
        temp_lst = extract_markdown_links(node.text)
        if len(temp_lst) == 0 and node.text != "":
            new_nodes.append(node)
            continue
        text = node.text
        for i in range(len(temp_lst)):
            sections = text.split(f"[{temp_lst[i][0]}]({temp_lst[i][1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(temp_lst[i][0], TextType.LINK, temp_lst[i][1]))
            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes
