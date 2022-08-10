#!/bin/usr/bash -x
# ENV
source .venv/bin/activate
# source .venv/Scripts/activate

pip install .
python -m pytest
echo "Running Mapper:"
# tail -f /catelas/shared/scripts/metadata_mapper/metadata_mapper/logging/json_mapper.log
metadata_mapper 
# | tail -f /catelas/shared/scripts/metadata_mapper/metadata_mapper/logging/mapper_controller.log 
# | tail -f /catelas/shared/scripts/metadata_mapper/metadata_mapper/logging/xml_mapper.log | tail -f /catelas/shared/scripts/metadata_mapper/metadata_mapper/logging/json_mapper.log
grep -re "^failed" metadata_mapper/logging/*.log --exclude-dir=metadata_mapper/logging/old --exclude=metadata_mapper/logging/failed.log >metadata_mapper/logging/failed.log
# ENV
# . /catelas/shared/test.sh
