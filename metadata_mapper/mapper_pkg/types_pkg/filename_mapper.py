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
    baseDir = os.path.normpath(
        "c:/Users/Daniel.Ginzberg/Documents/Projects/ecomms-scripts"
    )
    log_path = os.path.join(
        baseDir,
        "UAT",
        "onBox",
        "catelas",
        "shared",
        "scripts",
        "metadata_mapper",
        "metadata_mapper",
        "logging",
        "mappers",
        data_info.curr_date,
        "file_name_HCMC.log",
    )
    if not os.path.isdir(log_path) and not os.path.isdir(os.path.dirname(log_path)):
        os.mkdir(os.path.dirname(log_path))
    file_handler = logging.FileHandler(log_path, mode="a", encoding=None, delay=False)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
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
