# mapper_types/xml_mapper --

import json
from typing import OrderedDict
import xmltodict
import os
import glob
import sys
from pathlib import Path
from utils_pkg import data_info, mapper_files
from mapper_pkg.types_pkg import Json_Mapper


class Xml_Mapper(Json_Mapper):
    def __init__(self, files = mapper_files()):
        super().__init__(files)
        self.files = files

    def run_mapper(self):
        for file in self.files:
            in_dict = self.ingest_data(file)
            out_dict = super().map_data(in_dict, file.software)
            out_file = super().write_json(out_dict, file)
            super().super().successful += 1

    def flatten_dict(self, d):
        def items():
            for key, value in d.items():
                if isinstance(value, dict):
                    for subkey, subvalue in self.flatten_dict(value).items():
                        yield key + "." + subkey, subvalue
                else:
                    yield key, value

        return OrderedDict(items())

    def ingest_data(self, file):
        try:
            with open(file.file) as xml_file:
                try:
                    file.data_dict = self.flatten_dict(xmltodict.parse(xml_file.read()))
                    xml_file.close()
                    self.logger.debug("ingested data: %s", file.data_dict)
                except:
                    self.logger.error("failed to parse xml: %s", file.file)
        except:
            self.logger.error("failed to open file: %s", file.file)
