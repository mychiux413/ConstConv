origin_dir=$PWD

pytest tests && pip install . && \
create-multi-langs --from_csv data/valid_format.csv --to_file tests/go/generated.go && \
cd tests/go && \
go test

cd $origin_dir
create-multi-langs --from_csv data/valid_format.csv --to_file tests/python/generated.py && \
pytest tests/python/generated_t.py && rm tests/python/generated.py


create-multi-langs --from_csv data/valid_format.csv --to_file tests/python/generated_typing.py --py_typing && \
pytest tests/python/generated_typing_t.py && rm tests/python/generated_typing.py

create-multi-langs --from_csv data/valid_format.csv --to_file tests/typescript/generated_frontend.ts && \
ts-node tests/typescript/generated_frontend.test.ts && rm tests/typescript/generated_frontend.ts

create-multi-langs --from_csv data/valid_format.csv --to_file tests/typescript/generated_backend.ts --backend && \
ts-node tests/typescript/generated_backend.test.ts && rm tests/typescript/generated_backend.ts
