FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=graphqlapi.settings.production
WORKDIR /app/server/
COPY ./server /app/server/
RUN pip install --upgrade pip
RUN pip install -r requirements/prod.txt
