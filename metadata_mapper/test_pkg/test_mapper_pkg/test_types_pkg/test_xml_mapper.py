# test_types_pkg/test_xml_mapper --
import pytest
from mapper_pkg import Xml_Mapper
@pytest.mark.usefixtures("init_xml_mapper")
class TestXmlMapper:
    def test_xml_init(self, test_files):
        assert len(self.xml_mapper.files.all_files) == 2
        assert self.xml_mapper.files == test_files.get("xml_mapper_files")

    def test_xml_ingest_data(self, test_xml_file):
        file = test_xml_file.get("mapper_file")
        data_dict = test_xml_file.get("data_dict")
        self.xml_mapper.ingest_data(file)
        assert file.data_dict == data_dict
        for key in data_dict.keys():
            assert file.data_dict.get(key) == data_dict.get(key)

    # TEST_TODO: test run_xml_mapper
    def test_xml_run_mapper(self):
        pytest.xfail(reason="not implemented")

    # TEST_TODO: test_datetime_formater
    def test_xml_datetime_formater(self):
        pytest.xfail(reason="not implemented")

    # TEST_TODO: test run_mapper
    def test_xml_run_mapper(self):
        pytest.xfail(reason="not implemented")

    # TEST_TODO: test map_data
    def test_xml_map_data(self):
        pytest.xfail(reason="not implemented")

    # TEST_TODO: test write_json
    def test_xml_write_json(self):
        pytest.xfail(reason="not implemented")


pytest.main()
