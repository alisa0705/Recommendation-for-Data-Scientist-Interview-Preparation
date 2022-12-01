install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code
	black *.py alisa_library/*.py
#lint:
	#flake8 or #pylint
	#pylint --disable=R,C *.py alisa_library/*.py
#test:
	#test
	#python -m pytest -vv --cov=alisa_library *.py
build:
	#build container
	docker build -t deploy-fastapi .
run:
	#run docker
	
deploy:
	# push to ECR
	aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/h2g8h2a1
	docker build -t alisaproject4 .
	docker tag alisaproject4:latest public.ecr.aws/h2g8h2a1/alisaproject4:latest
	docker push public.ecr.aws/h2g8h2a1/alisaproject4:latest
all: install lint test 
