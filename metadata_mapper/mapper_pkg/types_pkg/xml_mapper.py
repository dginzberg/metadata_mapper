# mapper_types/xml_mapper --

import json
from typing import OrderedDict
import xmltodict
import os
import glob
import sys
from pathlib import Path
from utils_pkg import data_info, mapper_files, directories
from mapper_pkg.types_pkg import Json_Mapper


class Xml_Mapper(Json_Mapper):
    def __init__(self, files = mapper_files()):
        super().__init__(files)
        self.files = files

    def run_mapper(self, speechmatics_in_dir = directories.speechmatics_in_dir):
        self.logger_config()
        processed = []
        output = []
        failed = []
        for file in self.files.xml_files:
            self.logger.debug("mapping file: %s", file.file)
            try:
                self.ingest_data(file)
            except:
                self.logger.error("failed to ingest data from file: %s", file.file)
                failed.append(file)
                continue
            try:
                self.map_data(file)
            except:
                self.logger.error("failed to map file: %s, with data: %s", file.file, file.data_dict)
                failed.append(file)
                continue
            try:
                output.append(self.write_json(file, speechmatics_in_dir).name)
            except:
                self.logger.error("failed to write json: %s", file.file)
                failed.append(file)
                continue
            
            self.successful += 1
            processed.append(file)
        return (mapper_files(processed), mapper_files(output), mapper_files(failed))

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
            print("file:%s", file.file)
            with open(file.file) as xml_file:
                try:
                    file.data_dict = self.flatten_dict(xmltodict.parse(xml_file.read()))
                    xml_file.close()
                    self.logger.debug("ingested data: %s", file.data_dict)
                except:
                    self.logger.error("failed to parse xml: %s", file.file)
        except:
            self.logger.error("failed to open file: %s", file.file)
