#!/bin/usr/bash -x

source .venv/Scripts/activate
pip install .
metadata_mapper
grep -re "^failed" metadata_mapper/logging/*.log --exclude-dir=metadata_mapper/logging/old --exclude=metadata_mapper/logging/failed.log >metadata_mapper/logging/failed.log
python -m pytest
# ENV
. /catelas/shared/test.sh
