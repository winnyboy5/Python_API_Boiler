# Flask-Docker-Starter
A starter template Docker with FLASK, NGINX &amp; POSTGRES

## Development
Uses the default Flask development server.

Rename .env.dev-sample to .env.dev.

Update the environment variables in the docker-compose.yml and .env.dev files.

Build the images and run the containers:

$ docker-compose up -d --build

Test it out at http://localhost:5000. The "web" folder is mounted into the container and your code changes apply automatically.

## Production
Uses gunicorn + nginx.

Use .env.prod-sample to .env.prod and .env.prod.db-sample to .env.prod.db. Update the environment variables.

Build the images and run the containers:

$ docker-compose -f docker-compose.prod.yml up -d --build

Test it out at http://localhost:1337. No mounted folders. To apply changes, the image must be re-built.
