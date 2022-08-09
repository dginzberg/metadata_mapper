#!/bin/usr/bash -x

# ENV
source .venv/bin/activate
# source .venv/Scripts/activate

pip install .
python -m pytest
metadata_mapper
grep -re "^failed" metadata_mapper/logging/*.log --exclude-dir=metadata_mapper/logging/old --exclude=metadata_mapper/logging/failed.log >metadata_mapper/logging/failed.log
# ENV
. /catelas/shared/test.sh
