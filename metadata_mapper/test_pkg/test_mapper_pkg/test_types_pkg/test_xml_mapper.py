# test_types_pkg/test_xml_mapper --
from datetime import datetime
import os
import pytest
from mapper_pkg import Xml_Mapper
from utils_pkg import labels, directories

@pytest.mark.usefixtures("init_xml_mapper")
class TestXmlMapper:
    def test_xml_init(self, test_files):
        assert len(self.xml_mapper.files.all_files) == 2
        assert self.xml_mapper.files == test_files.get("xml_mapper_files")

    def test_xml_ingest_data(self, test_xml_file):
        for file in self.xml_mapper.files.all_files:
            self.xml_mapper.ingest_data(file)
            assert file.data_dict != None
            assert len(file.data_dict) == len(test_xml_file.get('data_dict')) or len(test_xml_file.get('data_dict'))+1
            for key in file.data_dict.keys():
                if key != "CAudioFile.Agent.GroupsList":
                    assert file.data_dict.get(key) != None

        file = test_xml_file.get("mapper_file")
        data_dict = test_xml_file.get("data_dict")
        self.xml_mapper.ingest_data(file)
        assert file.data_dict == data_dict
        for key in data_dict.keys():
            assert file.data_dict.get(key) == data_dict.get(key)

    # TEST_TODO: test_datetime_formater
    def test_xml_datetime_formater(self, test_datetime_format, test_info):
        for file in self.xml_mapper.files.all_files:
            # format = test_datetime_format.get(file.software)
            result_date = self.xml_mapper.datetime_formatter(test_datetime_format.get("IPC"))
            datetime.strptime(result_date, test_info.get("date_time_format"))
            
    def test_xml_get_date_label_data(self, test_info):
        for file in self.xml_mapper.files.all_files:
            result_date = self.xml_mapper.get_date_label_data(file, labels.out_label_ref[0])
            datetime.strptime(result_date, test_info.get("date_time_format"))
    
    # TEST_TODO: test map_data
    def test_xml_map_data(self, test_xml_file):
        for file in self.xml_mapper.files.all_files:
            self.xml_mapper.map_data(file)
            assert len(file.data_dict) ==  5
            for val in file.data_dict.values():
                assert val != None
        xml_file = test_xml_file.get("mapper_file")
        self.xml_mapper.map_data(xml_file)
        assert xml_file.data_dict == test_xml_file.get("out_dict")

    # TEST_TODO: test write_json
    def test_xml_write_json(self, test_info):
        for file in self.xml_mapper.files.all_files:
            out_file =self.xml_mapper.write_json(file, test_info.get("speechmatics_in_dir"))
            assert os.path.isfile(out_file.name)
    
    # TEST_TODO: test run_mapper
    def test_xml_run_mapper(self, test_info):
        processed, output, failed = self.xml_mapper.run_mapper(test_info.get("speechmatics_in_dir"))
        
        assert len(failed.all_files) == 0
        # assert self.xml_mapper.successful == 2
        assert len(processed.all_files) == 2
        assert len(output.all_files) == 2


pytest.main()
