lint:
	black .
sort:
	isort .
test:
	pytest tests/test.py

run:
	streamlit run main.py 
update_pip:
	pipreqs --force .
