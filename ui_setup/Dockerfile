FROM logstash:7.10.1

COPY logstash_http.conf /logstash_dir/

RUN logstash-plugin install logstash-input-http