# base image to use
FROM python:3.8

# attaching a label to my image
LABEL name=workshop01-task1

# take in or set some args
ARG WORK_DIR=/python

WORKDIR ${WORK_DIR}

COPY ${WORK_DIR} .

# install deps
RUN pip install -r requirements.txt

# expose some ports to external entities
ENV APP_PORT=3000

# run the app
ENTRYPOINT ./run.sh ${APP_PORT}
