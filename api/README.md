# Caveats
This project is using a single database. This is not ideal, but since it's a self hosted project, i couldn't justify the overhead of managing multiple databases.
In a real project, each application should have it's own database.

# General
- To start the project, run `docker-compose up`

# Alembic
All the commands below should be executed in the `web` docker environment.

- Add a new manual migration:  
`docker exec DOCKER_PROCESS_ID alembic revision -m "MIGRATION NAME"`, then procceed to edit the upgrade and downgrade functions on `/api/alembic/versions`
- Add a new automatically generated migration based on models:  
`docker exec DOCKER_PROCESS_ID alembic revision --autogenerate -m "MIGRATION NAME"`
- Apply to latest migration:  
`docker exec DOCKER_PROCESS_ID alembic upgrade head`
- Relative migration (upgrade or downgrade):  
`docker exec DOCKER_PROCESS_ID alembic upgrade +1`
`docker exec DOCKER_PROCESS_ID alembic downgrade -2`