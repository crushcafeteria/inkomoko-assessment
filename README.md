- Demo Link: <http://172.104.118.166:8000/dataset>
- Swagger API Documentation: <http://172.104.118.166:8000/docs>
- Adminer Link: <http://172.104.118.166:9999>

## Running the application

This application is built with FastAPI library and Python Docker container.

#### Running the Docker stack

To run the development server use the command below:

```
docker compose up -d --force-recreate --build
```

You can inspect Python packages installed in the container by opening `requirements.txt`.

#### Stopping the Docker stack

To stop the Docker stack:

```
docker compose down -v
```

You can inspect the Docker container laters by opening `Dockerfile`

## Previewing the data

You can access get all the items in the database in JSON format at this link:

- **Dataset Viewer** - <http://172.104.118.166:8000/dataset>

## SQL Schema

A sample `schema.sql` fil has been attached in the project root. To import this file, you can access Adminer using the details below and use its Import feature:

- Adminer Link: <http://172.104.118.166:9999>
- Username: `root`
- Password: `root`
- Database Name: `inkomoko`

## Tunneling via `localtunnel`

In order to receive requests on `localhost`, you need to run `localtunnel` to allow your local app accessible online with the following command.

```
lt --port 8000 -s inkomoko
```

Please adjust the subdomain correctly and make sure to register it to receive webhook data.
