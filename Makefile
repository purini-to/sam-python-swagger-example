BUILD_PATH = build/
APP_DIR = app
TEMPLATE_PATH = template.yaml
PACKAGE_PATH = packaged.yaml
STACK_NAME = sam-python-swagger-example
CFN_BUCKET = <your cloudformation upload bucket>
CFN_PREFIX = $(STACK_NAME)

.PHONY: default dep test clean build start-api package deploy

default: start-api

dep:
	pip install -r requirements.txt -c constraints.txt
	pip install -r test_requirements.txt -c constraints.txt

test:
	python -m pytest tests -v --cov=app/

clean:
	rm -rf $(BUILD_PATH) .coverage htmlcov

build: clean
	pip install -r requirements.txt -c constraints.txt -t $(BUILD_PATH)
	cp -Rf $(APP_DIR) build/$(APP_DIR)

start-api: build
	sam local start-api

package: build
	sam package \
	--template-file $(TEMPLATE_PATH) \
	--output-template-file $(PACKAGE_PATH) \
	--s3-bucket $(CFN_BUCKET) \
	--s3-prefix $(CFN_PREFIX)

deploy: package
	sam deploy \
	--template-file $(PACKAGE_PATH) \
	--stack-name $(STACK_NAME) \
	--capabilities CAPABILITY_IAM
