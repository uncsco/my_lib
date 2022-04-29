# bash init.sh

python3 -m poetry remove numpy

python3 -m poetry add --dev pytest
python3 -m poetry add --dev mypy

python3 -m poetry add pydantic