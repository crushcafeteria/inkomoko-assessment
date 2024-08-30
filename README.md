# Introduction

- Demo Link: <http://172.104.118.166:8000/dataset>
- Swagger API Documentation: <http://172.104.118.166:8000/docs>
- Adminer Link: <http://172.104.118.166:9999>

#### Setup

This application is built with FastAPI library, Python Docker container, Envoy TaskRunner and PyTest.

#### Running the application

To run the development server use the command below:

```
docker compose up -d --force-recreate --build
```

You can inspect Python packages installed in the container by opening `requirements.txt`.

#### Stopping the application

To stop the application, take down the Docker stack:

```
docker compose down -v
```

You can inspect the Docker container layers by opening `Dockerfile`

## Using the application

#### Accessing container environment

This application can be accessed primarily from its REST API.

If you want to access the container logs, please use the command below:

```
docker compose logs web
```

If you want to access the container bash terminal, please use the command below:

```
docker compose exec web bash
```

#### How to manually extract data from Kobo

Toe manually extract data from the API:

1. Access Swagger UI here: <http://172.104.118.166:8000/docs>
2. Click on the `/extract_records` section to reveal.
3. Next, click on `Try it out` then `Execute`
4. You should see a positive response in a few moments
5. Because the app processes data in the background, you should wait a few moments before checking for results.

#### Previewing database contents

To view your database contents, you have 3 options:

1. Open Adminer UI here: <http://172.104.118.166:9999>
2. Visit the `/dataset` URL here: <http://172.104.118.166:8000/dataset>
3. Access `/dataset` route in the Swagger UI

#### Receiving data in realtime with webhooks

To receive data in realtime, you must register a webhook with the data source. To register a webhook URL:

1. Access Swagger UI here: <http://172.104.118.166:8000/docs>
2. Click on the `/register_webhook` section to reveal
3. Enter your webhook URL and submit
4. You should see a positive response in a few moments

Now every time the form is filled, your registered webhook URL will receive a copy of the data.

You can check your app received the data by previewing the database contents using the methods described above.

## SQL Schema File

A sample `schema.sql` fil has been attached in the project root. To import this file, you can access Adminer using the details below and use its Import feature:

- Adminer Link: <http://172.104.118.166:9999>
- Username: `root`
- Password: `root`
- Database Name: `inkomoko`

## Automated Deployments

We use Laravel Envoy taskrunner to enable quick deployments. You can read more about Envoy by visiting their website.

First, make sure that you have copied your public key to the target server. Also ensure you have Docker installed and running on the target machine and all required ports have been opened.

Here is a list of all external ports used by this application.

- Port 8000: FastAPI REST Server
- Port 9999: Adminer Database UI

Next, ensure you have Composer installed in the local machine, then install the packages with:

```
composer install
```

A `composer.json` file is included if you want to inspect which packages will be installed.

To deploy the application, run the following command:

```
vendor/bin/envoy run deploy
```

A deployment file `Envoy.blade.php` has been included if you want to inspect which commands will be executed in your target server.

## Running Tests

To run unit tests, use the following command:

```
pytest
```

To inspect the unit tests, see the `test_main.py` file.

## Assumptions

In case you are running this application locally, you can use `ngrok` or `localtunnel` to bridge your LAN with the public internet and receive webhook messages.
