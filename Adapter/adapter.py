import json
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup, Tag, NavigableString

class AdapterInterface(ABC):
    @abstractmethod
    def get(self):
        pass

class Adapter(AdapterInterface):
    def __init__(self, adaptee: BeautifulSoup):
        self.adaptee = adaptee

    def get(self):
        return self.adaptee.get_text()

    def get_json(self):
        root = next((tag for tag in self.adaptee.find_all() if isinstance(tag, Tag)), None)
        if root is None:
            return json.dumps({})

        def xml_to_dict(element):
            if isinstance(element, NavigableString):
                text = element.strip()
                return text if text else None

            if not isinstance(element, Tag):
                return None

            children = [child for child in element.children if isinstance(child, Tag)]
            if not children:
                text = element.get_text(strip=True)
                return text

            result = {}
            for child in children:
                child_dict = xml_to_dict(child)
                if child.name in result:
                    if isinstance(result[child.name], list):
                        result[child.name].append(child_dict)
                    else:
                        result[child.name] = [result[child.name], child_dict]
                else:
                    result[child.name] = child_dict
            return result

        return json.dumps(xml_to_dict(root), indent=4)

    def export_json(self, filename="config.json"):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.get_json())
