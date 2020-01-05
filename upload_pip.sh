rm -rf dist build Create_Multi_Langs_mychiux413.egg-info &&\
python setup.py sdist bdist_wheel && \
twine check dist/* && \
twine upload dist/* --verbose