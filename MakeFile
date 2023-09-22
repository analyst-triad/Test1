install:
	pip install --upgrade pip&\
	pip install -r requirements.txt
test:
	pytest test.py
lint:
	pylint --disable=all --enable=syntax main.py


