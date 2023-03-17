FROM rabbitmq:management-alpine

RUN rabbitmq-plugins enable rabbitmq_prometheus

# port 15692 for prometheus
# port 5672 for python script
# port 15672 for GUI
