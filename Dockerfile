# Use an official Python image based on Alpine Linux
FROM python:3.9-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the Pipfile and Pipfile.lock into the container
COPY Pipfile Pipfile.lock /app/

# Install pipenv and project dependencies
RUN apk add --no-cache --virtual .build-deps build-base libressl-dev libffi-dev && \
    pip install pipenv && \
    pipenv install --deploy --ignore-pipfile && \
    apk del .build-deps

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the app using Gunicorn
CMD ["pipenv", "run", "gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
