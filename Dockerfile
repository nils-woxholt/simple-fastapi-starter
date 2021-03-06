# uses the build from scratch approach mentioned here: 
# https://fastapi.tiangolo.com/deployment/docker/
FROM python:3.9-slim-bullseye
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
EXPOSE 80
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]