# Instructions

## Python environment

```bash
python -m venv .venv
# or
python3 -m venv .venv
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run flask locally

```bash
cd app
uvicorn main:app --reload
```

## Docker commands - Optional

```bash
# build the container
docker build -t my-fastapi .

# run the container
docker run -p 8000:80 my-fastapi

# optionally run via docker-compose
docker-compose up
```

## Test the API

Now you can browse to <http://localhost:8000/>

If you have the Visual Studio Code REST Client extension installed, you can open test.http and click on the various endpoints to test.
