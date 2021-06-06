build: ## Build the container
	docker build -t marsrover .

api: ## Run container
	docker run -i --rm marsrover python3 marsrover/cli.py < input.txt

up: build api ## Run container

test: ## Stop and remove a running container
	docker run -i --rm marsrover python3 -m pytest tests
