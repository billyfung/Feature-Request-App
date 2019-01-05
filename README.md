# Feature-Request-App
Web application that allows the user to create feature requests

# Set up
Currently running app within docker containers
- skeleton production version
- within `/app` is where I'm developing and moving things over to proper structure 
- a bit backwards but works for now for a quick start

`docker-compose up -d` will start the Flask app, Postgres, and Nginx containers.
Located at http://localhost:8080/ 

## Feature Request Model
- Title
- Description
- Client : "Client A", "Client B", "Client C"
- Client Priority: integer priority keyed on client, unique 
- Target Date
- Product Area: 'Policies', 'Billing', 'Claims', 'Reports'
