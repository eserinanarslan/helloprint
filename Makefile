ifndef VERBOSE
.SILENT:
endif

execute-project:
	$(MAKE) deploy-requirements
	$(MAKE) execute-code

deploy-requirements:
	pip install -r requirements.txt

execute-code:
	python src/app.py