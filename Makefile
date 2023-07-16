PYTHONPATH := "."

.PHONY: run-cov
run-cov:
	 @echo "Run server with line coverage"
	 PYTHONPATH=${PYTHONPATH} coverage run -a manage.py start-test-app

.PHONY: run-branch-cov
run-branch-cov:
	@echo "Run server with branches coverage"
	PYTHONPATH=${PYTHONPATH} coverage run --branch -a manage.py start-test-app
