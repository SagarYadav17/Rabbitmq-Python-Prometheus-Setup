import pika
import sys
import os
import ast


def callback(ch, method, properties, body):
    try:
        print(ast.literal_eval(body.decode()))
    except SyntaxError:
        pass


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost"),
    )
    channel = connection.channel()

    channel.queue_declare(queue="hello")

    channel.basic_consume(
        queue="hello",
        on_message_callback=callback,
        auto_ack=True,
    )

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
