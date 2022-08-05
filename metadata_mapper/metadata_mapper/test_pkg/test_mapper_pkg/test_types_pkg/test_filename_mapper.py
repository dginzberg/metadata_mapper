# metadata_mapper/test_mapper_pkg/test_file_name_mapper --
from fileinput import filename
import pytest

# from mapper_pkg.types_pkg.filename_mapper import Filename_Mapper
# from test_pkg.testing_constants import test_vars
constants = []


class TestFilenameMapper:
    # TEST_TODO: test filename init
    def test_filename_init(self, test_files):
        pytest.xfail(reason="not implemented")

    # TEST_TODO: test filename ingestion
    def test_filename_ingest_data(self):
        pytest.xfail(reason="not implemented")

    # TEST_TODO: test run_filename_mapper
    def test_filename_run_mapper(self):
        pytest.xfail(reason="not implemented")

    # TEST_TODO: test_datetime_formater
    def test_filename_datetime_formater(self):
        pytest.xfail(reason="not implemented")

    # TEST_TODO: ingests_each file in mapper_files() object
    def test_filename_ingest_data(self):
        pytest.xfail(reason="not implemented")

    # TEST_TODO: test run_mapper
    def test_filename_run_mapper(self):
        pytest.xfail(reason="not implemented")

    # TEST_TODO: test map_data
    def test_filename_map_data(self):
        pytest.xfail(reason="not implemented")

    # TEST_TODO: test write_json
    def test_filename_write_json(self):
        pytest.xfail(reason="not implemented")


pytest.main()
