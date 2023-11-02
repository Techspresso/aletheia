venv:
	@echo "Creating virtual environment"
	@python3 -m venv venv
	@echo "Virtual environment created"
	@echo "Run 'source venv/bin/activate' to activate the virtual environment"

rmvenv:
	@echo "Removing virtual environment"
	@rm -rf venv
	@echo "Virtual environment removed"

install: venv
	@echo "Installing dependencies"
	pip3 install -e .
	@echo "Dependencies installed"

install-test-dependencies:
	@echo "Installing test dependencies"
	pip3 install .[test]
	@echo "Test dependencies installed"

test: 
	pytest