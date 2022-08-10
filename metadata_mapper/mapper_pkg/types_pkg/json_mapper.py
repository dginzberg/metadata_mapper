# mapper_types/json_mapper --

from cmath import log
import json

from utils_pkg import data_info, regions, labels, mapper_files, directories
from mapper_pkg.types_pkg import Mapper


class Json_Mapper(Mapper):
    def __init__(self, files=mapper_files()):
        super().__init__(files)

    def ingest_data(self, file):
        self.logger.info("Reading input file")
        self.logger.debug(file.file_dir + file.filename)
        with open(file.file, "r") as input_json:
            in_data = json.load(input_json)
            self.logger.debug("Data collected from file")
            self.logger.debug(str(in_data))
            file.data_dict = in_data

    def run_mapper(
        self,
        speechmatics_in_dir=directories.speechmatics_in_dir,
    ):
        self.logger_config()
        processed = []
        output = []
        failed = []
        self.logger.debug("running_mapper")
        for file in self.files.json_files:
            try:
                self.logger.debug("ingesting_data")
                self.logger.debug(file.file)
                self.ingest_data(file)
            except:
                self.logger.error("failed to ingest data from file: %s", file.file)
                failed.append(file)
                continue
            try:
                self.logger.debug("mapping data")
                self.map_data(file)
            except:
                self.logger.error("failed to map file: %s, with data: %s", file.file, file.data_dict)
                failed.append(file)
                continue
            try:
                output_file = self.write_json(file, speechmatics_in_dir).name
                self.logger.debug("writing output")
                self.logger.debug(output_file )
                output.append(output_file)
            except:
                self.logger.error("failed to write json: %s", file.file)
                failed.append(file)
                continue
            
            self.successful += 1
            processed.append(file)
        return (mapper_files(processed), mapper_files(output), mapper_files(failed))
