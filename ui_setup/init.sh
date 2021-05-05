mkdir -p .docker/elasticsearch/esdata/nodes
sudo chown -R 1000:1000 .docker/elasticsearch/esdata/nodes

docker-compose up