FROM python:3.11-alpine

ARG BRANCH="master"
ARG COMMIT=""
ENV COMMIT_SHA=${COMMIT}
ENV COMMIT_BRANCH=${BRANCH}
RUN mkdir /app
RUN apk add python3-dev build-base linux-headers pcre-dev
COPY ./src/ /app

RUN pip3 install -r /app/requirements.txt
ENV FLASK_APP=vs_query:app
WORKDIR /app
EXPOSE 5000
CMD [ "uwsgi", "-w", "vs_query:app", "--http-socket", ":5000" ]
ENTRYPOINT [ "./entrypoint.sh" ]
