# Feature-Request-App
Web application that allows the user to create feature requests

# Set up
Currently running app within docker containers
- within `/app` is where I'm developing and moving things over to proper structure
- a bit backwards but works for now for a quick start

`docker-compose up -d` will start a bunch of containers.
Plan is to have flask app, with redis + celery queue

Web app located at http://localhost:5000/
Celery monitor located at http://localhost:5555/

To Do:
- form placeholder text
- form date picker
- organise app into app folder
- organise app with blueprints
- integrate log handler
- integrate celery queue

## Feature Request Model
- Title
- Description
- Client : "Client A", "Client B", "Client C"
- Client Priority: integer priority keyed on client, unique
- Target Date
- Product Area: 'Policies', 'Billing', 'Claims', 'Reports'
