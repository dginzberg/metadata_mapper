# test_types_pkg/test_mapper_interface --

import pytest


class TestMapperInterface:
    def test_inter_init_(self):
        pytest.xfail(reason="Interface cannot be tested")

    def test_inter_final_logging(self):
        pytest.xfail(reason="Interface cannot be tested")

    def test_inter_get_process_memory(self):
        pytest.xfail(reason="Interface cannot be tested")

    def test_inter_datetime_formater(self):
        pytest.xfail(reason="Interface cannot be tested")

    def test_inter_write_json(self):
        pytest.xfail(reason="Interface cannot be tested")

    def test_inter_map_data(self):
        pytest.xfail(reason="Interface cannot be tested")


pytest.main()
