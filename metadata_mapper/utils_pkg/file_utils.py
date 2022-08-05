# utils_pkg/file_utils --

import json
import os
from utils_pkg import data_info, regions, directories


class mapper_file:
    file = ""
    region = ""
    languages = ""
    filename = ""
    file_dir = ""
    software = ""
    filetype = ""
    data_dict = None

    def __init__(self, file=""):
        self.file = file
        if file != "":
            self.set_region(file)
            self.set_filename(file)
            self.set_file_dir(file)
            self.set_software(file)
            self.set_filetype(file)

    def set_filename(self, file):
        if file != "":
            self.filename = os.path.basename(file)

    def set_file_dir(self, file):
        try:
            if file != "":
                self.file_dir = os.path.dirname(
                    (file.split(directories.ingestion_dir.split(os.sep)[-1]))[1]
                ).strip(os.sep)
        except:
            self.file_dir = os.path.dirname(file)
            # self.file_dir = os.path.dirname(file.split())

    def set_software(self, file):
        for software in data_info.software:
            if software in file:
                self.software = software
                break

    def set_region(self, file):
        for key in regions.lang_ref:
            if key in file:
                self.region = key
                self.languages = regions.lang_ref.get(key)
                break

    def set_filetype(self, file):
        curr_type = os.path.splitext(file)[1]
        for type in data_info.metadata:
            if curr_type == type:
                self.filetype = curr_type
                return
        for type in data_info.audio:
            if curr_type == type:
                self.filetype = curr_type
                return

    def set_data_dict(self, data_dict):
        self.data_dict = data_dict

    def change_filetype(self, type):
        file_split = os.path.split(self.file)
        self.file = os.path.join(file_split[0], type)
        filename_split = os.path.split(self.filename)
        self.filename = os.path.join(filename_split[0], type)
        self.filetype = type


class mapper_files:
    def __init__(self, files=[]):
        self.all_files = files
        self.json_files = []
        self.xml_files = []
        self.filename_files = []
        if files != [] and type(files[0]) != mapper_file:
            self.all_files = []
            for file in files:
                map_file = mapper_file(file)
                self.all_files.append(map_file)
        else:
            self.all_files = files
        self.xml_files = []
        self.json_files = []
        self.filename_files = []
        for file in self.all_files:
            if file.filetype == data_info.metadata[0]:
                self.xml_files.append(file)
            elif file.filetype == data_info.metadata[1]:
                self.json_files.append(file)
            else:
                self.filename_files.append(file)

    def get_files_by_software(self, software):
        result_files = []
        for file in self.all_files:
            if file.software == software:
                result_files.append(file)
        return result_files

    def get_files_by_region(self, region):
        result_files = []
        for file in self.all_files:
            if file.region == region:
                result_files.append(file)
        return result_files

    def get_files_by_type(self, type):
        if "json_files" == type:
            return self.json_files
        if "xml_files" == type:
            return self.xml_files
        if "filename_files" == type:
            return self.filename_files
