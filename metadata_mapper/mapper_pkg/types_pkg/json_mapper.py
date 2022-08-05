# mapper_types/json_mapper --

from cmath import log
import json

from utils_pkg import data_info, regions, labels, mapper_files, directories
from mapper_pkg.types_pkg import Mapper


class Json_Mapper(Mapper):
    def __init__(self, files=mapper_files()):
        super().__init__(files)

    def ingest_data(self, file):
        self.logger.debug("Reading input file: %s", file.file_dir + file.filename)
        with open(file.file, "r") as input_json:
            in_data = json.load(input_json)
            self.logger.debug("Data collected from file: %s", str(in_data))
            file.data_dict = in_data

    def run_mapper(
        self,
        speechmatics_dir=directories.speechmatics_dir,
    ):
        self.logger_config()
        processed = []
        output = []
        failed = []
        for file in self.files.json_files:
            self.logger.debug("mapping file: %s", file.file)
            try:
                self.ingest_data(file)
                self.map_data(file)
                output.append(self.write_json(file, speechmatics_dir).name)
                self.successful += 1
                processed.append(file)
            except:
                self.logger.error("failed to map file: %s", file.file)
                failed.append(file)
        return (mapper_files(processed), mapper_files(output), mapper_files(failed))
