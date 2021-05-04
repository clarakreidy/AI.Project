FROM alpine:3.13

RUN apk update && apk add bash curl

WORKDIR /tmp

COPY dashboard.ndjson .
COPY wizard.sh .

ENTRYPOINT sh wizard.sh

#RUN curl -X POST http://0.0.0.0:5601/api/saved_objects/_import?createNewCopies=true -H "kbn-xsrf: true" --form file=@dashboard.ndjson