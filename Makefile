##
# Environment Variables
##

export API_PORT?=5000
export FLASK_APP?=microblog
export FLASK_ENV?=development


#
# Install dependencies
#     make install
#
install:
	pip install -r requirements.txt


#
# Build
#
build:
	docker-compose build api

#
# Run
#
run:
	./boot.sh

#
# Stop services
#		make down
#
down:
	docker-compose down

#
# Start services
# 		make up
#
up:
	docker-compose up -d

#
# Tests
#		python -m unittest
#
test:
	python -m unittest

