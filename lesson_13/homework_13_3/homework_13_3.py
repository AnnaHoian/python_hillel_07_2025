"""
Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і повернення значення
timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо
"""

import xml.etree.ElementTree as ET
import logging

class XMLSearching:
    """
    class XMLSearching for reading XML file, searching by group/number,
    and logging timingExbytes/incoming data into the console

    Attributes:
    input_file - path to xml file

    Methods:
    LogConfig() - set log configuration
    xml_parsing_searching_logging():
    - parse xml
    - searching by group and number
    - logging timingExbytes and incoming values
    """

    def __init__(self, input_file):
        self.input_file = input_file
        self.LogConfig()

    def LogConfig(self):
        logging.basicConfig(
            level= logging.INFO,
            format= '%(asctime)s - %(levelname)s - %(message)s',
        )

    def xml_parsing_searching_logging(self):
        tree = ET.parse(self.input_file)
        root = tree.getroot()

        for group in root.findall('group'):
            number = group.find('number')
            if number is not None:
                timing_exbytes = group.find('timingExbytes')
                incoming = number.find('incoming')

                if timing_exbytes is not None:
                    logging.info(f"timingExbytes value: {timing_exbytes.text}")
                else:
                    logging.info(f"timingExbytes is not found")

                if incoming is not None:
                    logging.info(f"incoming value: {incoming.text}")
                else:
                    logging.info(f"incoming is not found")

xml_file = 'groups.xml'

XML_result = XMLSearching(xml_file)
XML_result.xml_parsing_searching_logging()