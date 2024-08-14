.PHONY: help build watch up down makemigrations migrate

all:
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

build: # Build docker images
	docker compose --project-directory . build

watch: # Watch docker containers
	docker compose --project-directory . watch

up: # Start docker containers
	docker compose --project-directory . up -d

down: # Stop docker containers
	docker compose --project-directory . down --remove-orphans -v

restart: down up # Down and up docker containers

makemigrations: # Make migrations
	docker compose --project-directory . run --rm api python manage.py makemigrations

migrate: # Migrate database
	docker compose --project-directory . run --rm api python manage.py migrate

generate_db: # Migrate database
	docker compose --project-directory . run --rm api python manage.py generate_db

clear_db: # Migrate database
	docker compose --project-directory . run --rm api python manage.py clear_db