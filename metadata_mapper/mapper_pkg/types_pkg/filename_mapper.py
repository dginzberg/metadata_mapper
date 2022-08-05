# types_pkg/filename_mapper --
import logging
import os
import re
import sys

# from app_pkg.mapper_pkg.types_pkg.file_name_mapper import Filename_Mapper
from utils_pkg import data_info, regions, labels
from mapper_pkg.types_pkg import Mapper

# import file_name_mapper


class Filename_Mapper(Mapper):
    files = []

    def __init__(self, files):
        self.files = files
        super().__init__(files)

    def ingest_data(self, file):
        data = re.split("-+|_+", file)
        out_dict = {}
        for key in labels.output_ref():
            if key == "languages":
                out_dict[key] = file.languages
            else:
                out_dict[key] = data[labels.ref_dict[file.software][key]]
        return out_dict

    def run_mapper(self):
        for file in self.files:
            out_dict = self.ingest_data(file)
            self.write_json(out_dict, file)
            super().successful += 1
        return super().successful
