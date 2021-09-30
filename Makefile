default: ## Run the application
	@. ./oscenv/bin/activate && python manage.py runserver

freeze: ## Freeze pip to requirements
	@. ./oscenv/bin/activate && pip freeze > requirements.txt

env: ## Installation of dependencies
	@-virtualenv oscenv
	. ./oscenv/bin/activate && pip install -r requirements.txt

lint: ## Run linters
	./oscenv/bin/black .

help: ## Prints the help for make
	@cat $(MAKEFILE_LIST) | grep -E '^[a-zA-Z_-]+:.*?## .*$$' | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
