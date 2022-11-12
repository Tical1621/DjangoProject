FROM python:3.10-alpine

ENV DEBUG=False \
    PYTHONPATH=/app

COPY ./requirements.txt app/

RUN pip install -r app/requirements.txt --no-cache-dir

COPY . app/

WORKDIR app/

EXPOSE 8000/tcp

# CMD is used instead of ENTRYPOINT to allow other use case easily like run migrations leveraging the same image
CMD ["gunicorn", "-b", "0.0.0.0:8000", "DjangoApi.wsgi:application", "--access-logfile", "-", "--error-logfile", "-"]

# Alternative CMDs:
# CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "--access-log", "-", "DjangoApi.asgi:application"] - run async webserver
# CMD ["celery", "beat", "-A", "DjangoApi"] - run Celery beat scheduler
# CMD ["celery", "worker", "-A", "DjangoApi"] - run Celery worker process
