FROM python:3.8-slim

WORKDIR /app

COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

COPY . .

CMD ["pipenv", "run", "gunicorn", "app:app", "-b", "0.0.0.0:5000"]
