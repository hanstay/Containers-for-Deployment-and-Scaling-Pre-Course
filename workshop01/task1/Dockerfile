# base image to use
FROM python:3.8

# main dir is this
ARG WORK_DIR=/python

WORKDIR ${WORK_DIR}

# attaching a label to my image
LABEL name=workshop01-python-web

# no need to copy since the work dir contains everything
COPY ${WORK_DIR} .

# install deps
RUN pip install -r requirements.txt

# expose some ports to external entities
ENV APP_PORT=3000

# run the app
ENTRYPOINT gunicorn -b ":${PORT:-3000}" --log-level debug main:app 
