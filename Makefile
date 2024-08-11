.PHONY: install test lint format all

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	python -m textblob.download_corpora

test:
	python -m pytest --cov=. --cov-report=xml

lint:
	pylint --disable=R,C *.py nlp_logic/*.py

format:
	black *.py nlp_logic

all: install lint test
