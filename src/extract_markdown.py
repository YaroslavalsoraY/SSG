import re

def extract_markdown_images(text):
    alt_texts = re.findall(r"\!\[(.*?)\]", text)
    img_urls = re.findall(r"\(.*?://.*?\..*?\)", text)
    result_lst = []
    for i in range(len(alt_texts)):
        result_lst.append((alt_texts[i], img_urls[i].replace("(", "").replace(")", "")))
    return result_lst


def extract_markdown_links(text):
    texts = re.findall(r"\[(.*?)\]", text)
    urls = re.findall(r"\(.*?://.*?\..*?\)", text)
    result_lst = []
    for i in range(len(texts)):
        result_lst.append((texts[i], urls[i].replace("(", "").replace(")", "")))
    return result_lst
