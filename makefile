init:
    pip install -r requirements.txt

test:
    py.test tests

.PHONY: init test

install:
    ( \
       source path/to/virtualenv/bin/activate; \
       pip install -r requirements.txt; \
    )
