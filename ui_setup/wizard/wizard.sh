#!/bin/bash

# Wait for Elasticsearch to start up before doing anything.
until curl -s http://elasticsearch:9200/_cat/health -o /dev/null; do
    echo Waiting for Elasticsearch...
    sleep 1
done


# Wait for Kibana to start up before doing anything.
until curl -s http://kibana:5601/api/task_manager/_health -o /dev/null; do
    echo Waiting for Kibana...
    sleep 1
done

cd /tmp

#load dashboard
curl -X POST http://kibana:5601/api/saved_objects/_import?createNewCopies=true -H "kbn-xsrf: true" --form file=@dashboard.ndjson
