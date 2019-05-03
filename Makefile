ifndef VERBOSE
.SILENT:
endif

SHELL := '.'

execute-project:
	$(MAKE) deploy-requirements
	$(MAKE) execute-code

deploy-requirements:
	SHELL pip install -r requirements.txt

execute-code:
	SHELL python src/app.py


