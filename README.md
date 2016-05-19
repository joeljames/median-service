The application is setup to run locally with a docker container.

## Set up Docker Environment (Mac)
I use Mac for local development. Below are the instructions to set up
Docker on Mac

1. Install [Dinghy](https://github.com/codekitchen/dinghy)

2. Install [docker toolbox](https://www.docker.com/products/docker-toolbox)

3. Install [Virtual Box](https://www.virtualbox.org/wiki/Downloads)

4. Creat the docker-machine VM. Make sure to alocate enough resources to the VM.

    ``` bash
    $ dinghy create --disk=60000 --provider=virtualbox
    ```

5. Start the Docker VM and services

    ``` bash
    $ dinghy up
    ```

## Getting Started
This app is set up to run within a Docker Container.
The tools and steps required to run this application is defined within the
`Dockerfile` which is present at the root of the project directory.
The app processes (database and web) are defined within `docker-compose-base.yml` and `docker-compose.yml`.

Below are the steps to build and get the container up and running.

A list of make commands are available for managing tasks. You can view the list by running `make help` command.

1. Build the image:

    ``` bash
    $ docker-compose build
    ```

2. Seed the database with fixtures:

    ``` bash
    $ docker-compose run web make seed_db
    ```

3. Start the server:

    ``` bash
    $ docker-compose up
    ```

4. Check the server is up and running by hitting the url `http://median.docker/median`.


## Running Tests
All modules have tests written.

1. Running tests with coverage

    ``` bash
    $ docker-compose run web make test
    ```

## Running Lints
Checks to make sure that the code written are asper pep8, pyflakes standards

1. Install flake8

    ``` bash
    $ sudo pip3 install flake8
    ```

2. Run Lint

    ``` bash
    $ make lint
    ```

## API Documentation
This app opens up two endpoints

1. PUT `http://median.docker` which takes in an integer

    ```
    GET http://median.docker

    Request:

    Body:
        {
            "value": 3
        }


    Response:
        201

    Headers:
        Content-Type: application/json

    Body:
        {
            "message": "Value successfully created.",
            "status": 201
        }
    ```


2. GET `http://median.docker/median`  returns the median for all the values for the last minute

    ```
    GET http://median.docker/median

    Response:
        200

    Headers:
        Content-Type: application/json

    Body:

        {
            "median": 3
        }
    ```
