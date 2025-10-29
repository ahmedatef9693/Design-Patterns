import os
from bs4 import BeautifulSoup
from adapter import Adapter
xml_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.xml")

with open(xml_file_path, encoding="utf-8") as f:
    bs = BeautifulSoup(f, "lxml-xml")

adapter = Adapter(bs)
adapter.export_json()
