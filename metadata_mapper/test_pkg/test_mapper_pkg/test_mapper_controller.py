import os
import pytest

# from mapper_pkg.mapper_controller import Mapper_Controller
from mapper_pkg.mapper_controller import Mapper_Controller
from utils_pkg import directories


@pytest.mark.usefixtures("init_controller")
class TestMapperController:
    def test_ingest_files(self):
        self.controller.ingest_files()
        assert len(self.controller.files.all_files) == 18

    def test_map_files(self, test_info):

        for file in os.listdir(test_info.get("speechmatics_dir")):
            os.remove(os.path.join(test_info.get("speechmatics_dir"), file))
        result = self.controller.map_files()
        assert len(self.controller.failed_files) == 0
        assert len(self.controller.processed_files) == 10
        assert len(self.controller.output_files) == 10

        for file in self.controller.processed_files:
            out_file = os.path.join(test_info.get("speechmatics_dir"), file.filename.split('.')[0]+'.json')
            assert os.path.isfile(out_file)

    def test_processed(self, test_files, test_info):
        pass
        # for file in os.path.normpath(test_info.get("processed_dir")):
        #     os.remove(os.path.join(test_info.get("processed_dir"), file))

        # for file in os.listdir(test_info.get("ingestion_dir")):
        #     os.rename()
        # assert self.controller.processed_files == test_files.get("json_mapper_files")

        # self.controller.processed()

        # for file in self.controller.processed_files.all_files:
        #     out_dir = os.path.join(
        #         test_info.get("processed_dir"), file.file_dir, file.filename
        #     )
        #     assert os.path.isfile(out_dir)

    # TEST_TODO: test start_mapping
    def test_start_mapping(self):
        pytest.xfail(reason="not implemented")


pytest.main()
