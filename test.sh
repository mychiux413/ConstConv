origin_dir=$PWD

pytest tests && pip install . && \
create-multi-langs data/valid_format.csv tests/go/generated.go && \
cd tests/go && \
go test

cd $origin_dir
create-multi-langs data/valid_format.csv tests/python/generated.py && \
pytest tests/python/generated_t.py && rm tests/python/generated.py


create-multi-langs data/valid_format.csv tests/python/generated_typing.py --py_typing && \
pytest tests/python/generated_typing_t.py && rm tests/python/generated_typing.py

create-multi-langs data/valid_format.csv tests/typescript/generated_frontend.ts && \
ts-node tests/typescript/generated_frontend.test.ts && rm tests/typescript/generated_frontend.ts

create-multi-langs data/valid_format.csv tests/typescript/generated_backend.ts --backend && \
ts-node tests/typescript/generated_backend.test.ts && rm tests/typescript/generated_backend.ts

create-multi-langs data/valid_format.csv tests/javascript/generated_frontend.mjs && \
node --experimental-modules tests/javascript/generated_frontend.test.mjs && rm tests/javascript/generated_frontend.mjs

create-multi-langs data/valid_format.csv tests/javascript/generated_backend.mjs --backend && \
node --experimental-modules tests/javascript/generated_backend.test.mjs && rm tests/javascript/generated_backend.mjs

