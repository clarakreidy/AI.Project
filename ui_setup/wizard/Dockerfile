FROM alpine:3.13

RUN apk update && apk add bash curl

WORKDIR /tmp

COPY wizard.sh .
COPY dashboard.ndjson .

ENTRYPOINT sh wizard.sh