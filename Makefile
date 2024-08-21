install_reqs:
	@echo "Installing required Dependencies"
	@pip install -r requirements.txt
	@echo "Completed Requirements Installation"

data_ingestion: 
	@echo "Starting Data Ingestion Process"
	python src/components/data_ingestion.py
	@echo "Completed Data Ingestion"