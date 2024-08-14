SFT TEST TASK

## Contents

- - - 

- [Stack](#stack)
- [Installation](#installation)
- [Run](#run)
- [Documentation](#documentation)
- [Features](#features)

## Stack:

- - - 

* Python 3.12
* django 5.1
* djangorestframework 3.15.2

## Installation:

#### 1. Go to IDE and run in terminal:

   ```bash
   git clone https://github.com/VitaStain/sft_test_task.git
   ```

#### 2. Set env variables in .env file (an example can be found in the file ".env.example"

  ```bash
  cp .env.example .env
  ```

## Run:

#### 1.Build:

   ```bash
   make build
   ```

#### 2. Migrate:

   ```bash
   make migrate
   ```

#### 3. Run:

   ```bash
   make up
   ```

## Documentation

- - - 

- Swagger. Check on http://127.0.0.1:8000

## Features

#### Set database fake data:

   ```bash
   make generate_db
   ```

#### Clear database:

   ```bash
   make clear_db
   ```