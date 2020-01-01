origin_dir=$PWD

pip install . && \
create-multi-langs --from_csv data/valid_format.csv --to_file tests/go/generated.go && \
cd tests/go && \
go test

cd $origin_dir
create-multi-langs --from_csv data/valid_format.csv --to_file tests/python/generated.py && \
pytest tests/python/generated_t.py
