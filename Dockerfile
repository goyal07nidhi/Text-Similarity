FROM tiangolo/meinheld-gunicorn-flask:python3.7

ARG PROJECT_ROOT="."
ARG PROJECT_MOUNT_DIR="/"

ADD $PROJECT_ROOT $PROJECT_MOUNT_DIR

WORKDIR $PROJECT_MOUNT_DIR

COPY /app .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "/app/app.py" ]