# Invera ToDo-List Challenge (Python/Django Jr-SSr)

## Requisitos
- Tener Docker y Docker Compose instalado
## Instalacion
- Crear archivo `.env` (podes copiar el `.env.sample` y renombrarlo)
- *(OPCIONAL)* Para utilizar SQLITE en lugar de posgresql colocar variable de entorno `DJANGO_SETTINGS_MODULE=todo_app.settings-sqlite`
- Ejecutar el comando `sudo docker-compose up -d`
- Correr las migraciones `sudo docker exec todo-challenge_web_1 python manage.py migrate`
- El API correra en la ruta: `http://localhost:8000/` (Ruta a usar para este ejercicio `http://localhost:8000/api/v1/todos/task/`)

## Notas
- Comitie un archivo sqlite con 3 tareas para que no tengan que crear
- ABM de tareas
  - Para eliminar utilizar `DELETE` a `http://localhost:8000/api/v1/todos/task/${ID}`
  - Para marcar una tarea como completado utilizar `PATCH` en `http://localhost:8000/api/v1/todos/task/${ID}` con un body `{done: true}`
  - Para crear utilizar `POST` en `http://localhost:8000/api/v1/todos/task/`
  - Para ver la lista de tareas utilizar `GET` en `http://localhost:8000/api/v1/todos/task/`
    - Filtros para esta ruta (queries):
      - Para filtrar por fecha:
        - created_at__lte=2017-6-28+00:00
        - created_at__gte=2017-6-28+00:00
        - created_at=2017-6-28+00:00
      - Para filtrar por contenido
        - description__icontains=comprar
        - name__icontains=gimnacio
- Nunca utilice logs ni realice test en Django