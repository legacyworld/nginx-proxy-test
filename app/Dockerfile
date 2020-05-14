FROM python:alpine
USER root
RUN apk add gcc build-base linux-headers
RUN pip3 install flask uwsgi
WORKDIR /src
ENV PORT=80
ENV PYTHONUNBUFFERED=1
RUN adduser -S uwsgiusr
USER uwsgiusr
ENTRYPOINT ["uwsgi","--ini","/src/uwsgi.ini"]