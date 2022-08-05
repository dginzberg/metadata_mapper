# mapper_types/xml_mapper --

import json
from typing import OrderedDict
import xmltodict
import os
import glob
import sys
from pathlib import Path
from utils_pkg import data_info
from mapper_pkg.types_pkg import Json_Mapper


class Xml_Mapper(Json_Mapper):
    def __init__(self, files):
        super().__init__(self, files)
        self.files = files

    def run_mapper(self):
        for file in self.files:
            in_dict = self.ingest_data(file)
            out_dict = super().map_data(in_dict, file.software)
            out_file = super().write_json(out_dict, file)
            super().super().successful += 1

    def ingest_data(file):
        with open(file) as xml_file:
            in_dict = xmltodict.parse(xml_file.read())
            xml_file.close()
        return in_dict
