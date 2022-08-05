# test_types_pkg/test_json_mapper --
from datetime import datetime
import re
from pyparsing import empty
import pytest
from utils_pkg import data_info, mapper_file, directories
from mapper_pkg.types_pkg import Json_Mapper
import os


class TestJsonMapper:
    def test_json_init(self, test_files):
        mapper = Json_Mapper(test_files["json_mapper_files"])

        assert mapper.start_time is not None
        assert mapper.files == test_files.get("json_mapper_files")
        assert mapper.successful == 0
        assert os.path.exists(mapper.log_file) and os.path.isfile(mapper.log_file)

    def test_json_datetime_formater(self, test_files, test_datetime_format):
        mapper = Json_Mapper(test_files["json_mapper_files"])
        for file in mapper.files.all_files:
            format = test_datetime_format.get(file.software)

            date_time = mapper.datetime_formatter(format)

            datetime.strptime(date_time, data_info.date_time_format)

    def test_json_ingest_data(self, test_json_file):
        mapper = Json_Mapper()
        file = test_json_file.get("mapper_file")

        mapper.ingest_data(file)

        assert len(file.data_dict) == 7
        for key in test_json_file.get("data_dict").keys():
            assert file.data_dict.get(key) == test_json_file.get("data_dict").get(key)

    def test_get_date_labels(self, test_json_file):
        mapper = Json_Mapper()
        file = test_json_file.get("mapper_file")
        file.set_data_dict(test_json_file.get("data_dict"))

        date_data = mapper.get_date_label_data(file)

        assert date_data == test_json_file.get("date_data")

    def test_json_map_data(self, test_json_file, test_info):
        mapper = Json_Mapper()
        file = test_json_file.get("mapper_file")
        file.set_data_dict(test_json_file.get("data_dict"))

        mapper.map_data(file)

        assert test_json_file.get("out_dict") == file.data_dict

    def test_json_write_json(self, test_info, test_json_file):
        directories.speechmatics_dir = test_info.get("speechmatics_dir")
        mapper = Json_Mapper()
        file = test_json_file.get("mapper_file")
        file.data_dict = test_json_file.get("out_dict")

        out_file = mapper.write_json(file, test_info.get("speechmatics_dir"))

        assert os.path.isfile(out_file.name)

    def test_json_run_mapper(self, test_info, test_files):
        directories.speechmatics_dir = test_info.get("speechmatics_dir")
        mapper = Json_Mapper(test_files.get("json_mapper_files"))

        processed, output, failed = mapper.run_mapper()

        assert len(failed.all_files) == 0
        assert mapper.successful == 9
        assert len(processed.all_files) == 9
        assert len(output.all_files) == 9

        for file in processed.all_files:
            for field in file.data_dict.values():
                assert field
        for file in output.all_files:
            assert os.path.isfile(file.file)


pytest.main()
