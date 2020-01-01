pip install . && \
create-multi-langs --from_csv data/valid_format.csv --to_file tests/go/generated.go && \
cd tests/go && \
go test