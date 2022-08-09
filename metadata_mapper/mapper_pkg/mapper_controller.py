# mapper_pkg/mapper_controller --
# TODO: change move distutils is depricated
from calendar import c
from distutils.file_util import move_file
import os
from posixpath import dirname
from sys import stdout
import logging
import sys

from utils_pkg import directories, mapper_files

from mapper_pkg.types_pkg import Filename_Mapper, Json_Mapper, Xml_Mapper


class Mapper_Controller:
    def __init__(
        self,
        ingestion_dir=directories.ingestion_dir,
        processed_dir=directories.processed_dir,
        speechmatics_dir=directories.speechmatics_dir,
        transcribed_dir=directories.transcribed_dir,
        output_dir=directories.output_dir,
    ):
        self.files = []
        self.processed_files = []
        self.output_files = []
        self.failed_files = []
        self.ingestion_dir = ingestion_dir
        self.processed_dir = processed_dir
        self.speechmatics_dir = speechmatics_dir
        self.transcribed_dir = transcribed_dir
        self.output_dir = output_dir
        self.logger_config()


    def logger_config(self):
            self.log_file = os.path.join(
                directories.log_dir, self.__module__.split(".")[-1]+ ".log"
            )
            if not os.path.isdir(os.path.dirname(self.log_file)):
                os.mkdir(os.path.dirname(self.log_file))
            if not os.path.isfile(self.log_file):
                with open(self.log_file, "w") as outfile:
                    outfile.close
            self.file_handler = logging.FileHandler(
                self.log_file, mode="a", encoding=None, delay=False
            )
            self.logger = logging.getLogger()
            self.logger.addHandler(self.file_handler)
            self.logger.setLevel(logging.DEBUG)

    def submit_transcribed(self):
        for file in os.listdir(self.transcribed_dir):
            os.rename(
                os.path.join(self.transcribed_dir, file),
                os.path.join(self.output_dir, file.file_dir,  file.filename),
            )

    def ingest_files(self):
        for root, d_names, f_names in os.walk(self.ingestion_dir):
            self.logger.debug('root: %s', root)
            for f in f_names:
                try:
                    f = os.path.join(root, f)
                    self.logger.debug('ingest file: %s', f)
                    self.files.append(f)
                except:
                    self.logger.error("failed to ingest file: %s", f)
        self.logger.debug('ingested files: %s', self.files)
        self.files = mapper_files(self.files)
        

    def map_files(self):
        if len(self.files.xml_files) > 0:
            self.logger.debug('starting xml_mapper')
            try:
                xml_mapper = Xml_Mapper(self.files)
                xml_processed, xml_output, xml_failed = xml_mapper.run_mapper(
                    self.speechmatics_dir
                )
                self.processed_files = self.processed_files + xml_processed.all_files
                self.output_files = self.output_files + xml_output.all_files
                self.failed_files = self.failed_files + xml_failed.all_files
                self.logger.info('successful XML: %d processed_xml_files: %s, output_xml_files: %s failed_xml_files: %s', xml_mapper.successful,  self.processed_files, self.output_files, self.failed_files)
            except:
                self.logger.error("failed to run xml mapper")
        if len(self.files.json_files) > 0:
            self.logger.debug('starting json_mapper')
            try:
                json_mapper = Json_Mapper(self.files)
                json_processed, json_output, json_failed = json_mapper.run_mapper(
                    self.speechmatics_dir
                )
                self.processed_files = self.processed_files + json_processed.all_files
                self.output_files = self.output_files + json_output.all_files
                self.failed_files = self.failed_files + json_failed.all_files
                self.logger.info('successful JSON: %d processed_json_files: %s, output_json_files: %s failed_json_files: %s', json_mapper.successful,  self.processed_files, self.output_files, self.failed_files)
            except:
                self.logger.error("failed to run json mapper")
           
        # if len(self.files.filename_files) > 0:
        #     self.logger.debug('starting filename_mapper')
        #     try:
        #         filename_mapper = Filename_Mapper(self.files)
        #         filename_processed, filename_output, filename_failed = filename_mapper.run_mapper(
        #             self.speechmatics_dir
        #         )
        #         self.processed_files = self.processed_files + filename_processed.all_files
        #         self.output_files = self.output_files + filename_output.all_files
        #         self.failed_files = self.failed_files + filename_failed.all_files
        #         self.logger.info('successful Filename: %d processed_filename_files: %s, output_filename_files: %s failed_filename_files: %s', filename_mapper.successful,  self.processed_files, self.output_files, self.failed_files)
        #     except:
        #         self.logger.error("failed to run filename mapper")

    def mv_processed(self):
        for file in self.processed_files:
            move_dir = self.processed_dir + file.file_dir
            if not os.path.isdir(move_dir):
                os.makedirs(move_dir)
            os.rename(file.file, os.path.join(move_dir, file.filename))

    def start_mapping(self):
        # self.submit_transcribed()
        self.ingest_files()
        self.map_files()
        # self.mv_processed()


if __name__ == "__main__":
    controller = Mapper_Controller()
    controller.submit_transcribed()
    controller.start_mapping()
