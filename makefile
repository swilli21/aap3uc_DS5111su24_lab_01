#!/bin/bash

default:
	@cat makefile

pg17192.txt:
	bash get_texts.sh

raven_line_count:
	bash raven_line_count.sh

raven_word_count:
	bash raven_word_count.sh

raven_counts:
	bash raven_counts.sh

total_lines:
	bash total_lines.sh

total_words:
	bash total_words.sh

env:
	python3 -m venv env; source env/bin/activate; pip install --upgrade pip;

update: env
	source env/bin/activate; pip install -r requirements.txt

lint:
	pylint src/pkg_aap3uc/tokenize.py
