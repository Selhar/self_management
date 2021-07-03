# Alembic
All the commands below should be executed in the `web` docker environment.

- Add a new migration:  
`docker exec DOCKER_PROCESS_ID alembic revision -m "MIGRATION NAME"`, then procceed to edit the upgrade and downgrade functions on `/api/alembic/versions`
- Apply to latest migration:  
`docker exec DOCKER_PROCESS_ID alembic upgrade head`
- Relative migration (upgrade or downgrade):  
`docker exec DOCKER_PROCESS_ID alembic upgrade +1`
`docker exec DOCKER_PROCESS_ID alembic downgrade -2`