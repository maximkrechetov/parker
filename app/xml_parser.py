from lxml import etree
import requests


class XmlParser:
    def __init__(self, input_path):
        self.input_path = input_path

    def parse(self):
        xml = open(self.input_path, 'rb')
        content = xml.read()
        root = etree.XML(content)

        for node in root.getchildren():
            for elem in node.getchildren()[:10]:
                text = elem.text or 'None'
                print(elem.tag + " => " + text)
                try:
                    r = requests.head(elem.text)
                    print(r.status_code)
                except:
                    print("failed to connect")
