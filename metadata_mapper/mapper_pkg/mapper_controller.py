# mapper_pkg/mapper_controller --
# TODO: change move distutils is depricated
from calendar import c
from distutils.file_util import move_file
import os
from posixpath import dirname
from sys import stdout

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

    def submit_transcribed(self):
        for file in os.listdir(self.transcribed_dir):
            os.rename(
                os.path.join(self.transcribed_dir, file),
                os.path.join(self.output_dir, file),
            )

    def ingest_files(self):
        for root, d_names, f_names in os.walk(self.ingestion_dir):
            for f in f_names:
                f = os.path.join(root, f)
                self.files.append(f)
        self.files = mapper_files(self.files)

    def map_files(self):
        # PLAN: add xml_mapper initator once XML_Mapper is done
        """if len(files.xml) > 0:
        xml_mapper = Xml_Mapperles.xml)
        self.processed_files.append(xml_mapper.run_mapper())"""
        if len(self.files.json_files) > 0:
            # PLAN: exception handling on failure on mapping to continue upon failure
            json_mapper = Json_Mapper(self.files)
            json_processed, json_output, json_failed = json_mapper.run_mapper(
                self.speechmatics_dir
            )
            self.processed_files = self.processed_files + json_processed.all_files
            self.output_files = self.output_files + json_output.all_files
            self.failed_files = self.failed_files + json_failed.all_files
            # PLAN: add filename_mapper initator once Filename_Mapper is done
        """ if len(files.filename) > 0:
            filename_mapper = Filename_Mapper(files.filename)
            self.processed_files.append( filename_mapper.run_mapper()) """

    def mv_processed(self):
        for file in self.processed_files:
            move_dir = self.processed_dir + file.file_dir
            if not os.path.isdir(move_dir):
                os.makedirs(move_dir)
            os.rename(file.file, os.path.join(move_dir, file.filename))

    def start_mapping(self):
        self.ingest_files()
        self.map_files()
        # self.mv_processed()
        print( self.processed_files)
        print(self.output_files)
        print(self.failed_files)


if __name__ == "__main__":
    controller = Mapper_Controller()
    controller.submit_transcribed()
    controller.start_mapping()
