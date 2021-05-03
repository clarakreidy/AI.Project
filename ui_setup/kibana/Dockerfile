FROM kibana:7.10.1

WORKDIR /app

COPY dashboard.ndjson .

RUN curl -X POST 0.0.0.0:5601/api/saved_objects/_import?createNewCopies=true -H "kbn-xsrf: true" --form file=@dashboard.ndjson