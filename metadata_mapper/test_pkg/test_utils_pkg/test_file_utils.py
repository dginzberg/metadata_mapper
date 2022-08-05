import os

import pytest
from utils_pkg import directories, mapper_file, mapper_files

# from test_pkg import test_file, test_files, test_audio_file


class TestMapperFile:
    def test_init_metadata(self, test_json_file, test_info):
        mapper_file(test_json_file["file"])
        directories.ingestion_dir = test_info.get("ingestion_dir")
        assert test_json_file["mapper_file"].file == test_json_file["file"]
        assert test_json_file["mapper_file"].filetype == test_json_file["filetype"]
        assert test_json_file["mapper_file"].filename == test_json_file["filename"]
        assert test_json_file["mapper_file"].file_dir == test_json_file["file_dir"]
        assert test_json_file["mapper_file"].software == test_json_file["software"]
        assert test_json_file["mapper_file"].region == test_json_file["region"]

    def test_init_audio(self, test_audio_file, test_info):
        directories.ingestion_dir = test_info.get("ingestion_dir")
        assert test_audio_file["mapper_file"].file == test_audio_file["file"]
        assert test_audio_file["mapper_file"].filetype == test_audio_file["filetype"]
        assert test_audio_file["mapper_file"].filename == test_audio_file["filename"]
        assert test_audio_file["mapper_file"].file_dir == test_audio_file["file_dir"]
        assert test_audio_file["mapper_file"].software == test_audio_file["software"]
        assert test_audio_file["mapper_file"].region == test_audio_file["region"]

    def test_set_data_dict(self, test_json_file):
        file = mapper_file()
        file.set_data_dict(test_json_file.get("data_dict"))
        assert file.data_dict == test_json_file.get("data_dict")

    def test_change_file_type(self, test_json_file, test_info):
        xml_type = test_info.get("metadata")[1]
        file = mapper_file(test_json_file.get("file"))
        file.change_filetype(xml_type)
        assert os.path.split(file.file)[1] == xml_type
        assert file.filetype == xml_type
        assert os.path.split(file.filename)[1] == xml_type


class TestMapperFiles:
    # example_files = file_utils.mapper_files(test_files.mix_files)

    def test_get_files_by_software(self, test_files, test_xml_file, test_info):
        directories.ingestion_dir = test_info.get("ingestion_dir")
        ipc_files = test_files.get("mix_mapper_files").get_files_by_software(
            test_xml_file.get("software")
        )
        assert len(ipc_files) == 2
        assert len(test_files.get("mix_mapper_files").all_files) == 18

    def test_get_files_by_region(self, test_files, test_xml_file, test_info):
        directories.ingestion_dir = test_info.get("ingestion_dir")
        MBB_HK_files = test_files.get("mix_mapper_files").get_files_by_region(
            test_xml_file.get("region")
        )
        assert len(MBB_HK_files) == 1
        assert len(test_files.get("mix_mapper_files").all_files) == 18

    def test_get_files_by_type(self, test_files, test_info):
        directories.ingestion_dir = test_info.get("ingestion_dir")
        json_files = test_files.get("mix_mapper_files").get_files_by_type("json_files")
        assert len(json_files) == 8
        assert len(test_files.get("mix_mapper_files").all_files) == 18
        assert len(test_files.get("mix_mapper_files").json_files) == 8

    def test_init_(self, test_files, test_info):
        directories.ingestion_dir = test_info.get("ingestion_dir")
        assert len(test_files.get("mix_mapper_files").all_files) == 18
        assert len(test_files.get("mix_mapper_files").json_files) == 8
        assert len(test_files.get("mix_mapper_files").filename_files) == 8
        assert len(test_files.get("mix_mapper_files").xml_files) == 2
        for file in test_files.get("mix_mapper_files").all_files:
            assert file.file != ""
            assert file.region != ""
            assert file.languages != ""
            assert file.filename != ""
            assert file.file_dir != ""
            assert file.software != ""
            assert file.filetype != ""


pytest.main()
