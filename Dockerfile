FROM python:3.11.1-slim-bullseye

# Install dependencies
RUN pip install poetry

# Workspace
WORKDIR /usr/src/check-it-out

COPY pyproject.toml poetry.lock src ./

# Install dependencies
RUN poetry export -f requirements.txt > requirements.txt
RUN pip install -r requirements.txt
CMD ["python", "main.py"]