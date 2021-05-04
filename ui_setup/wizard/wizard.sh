#!/bin/bash

# Wait for Elasticsearch to start up before doing anything.
until curl -s http://elasticsearch:9200/_cat/health -o /dev/null; do
    echo Waiting for Elasticsearch...
    sleep 10
done


# Wait for Kibana to start up before doing anything.
until curl -s http://kibana:5601api/task_manager/_health -o /dev/null; do
    echo Waiting for Kibana...
    sleep 10
done

cd /tmp
sleep 10

#load dashboard
curl -X POST http://kibana:5601/api/saved_objects/_import?createNewCopies=true -H "kbn-xsrf: true" --form file=@dashboard.ndjson

#load data

#until $(curl -X POST http://kibana:5601/api/saved_objects/_import?createNewCopies=true -H "kbn-xsrf: true" --form file=@dashboard.ndjson) != 'Kibana server is not ready yet'; do
#    echo Waiting for Kibana...
#    sleep 10
#done
