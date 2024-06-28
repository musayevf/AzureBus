from azure.servicebus import ServiceBusClient
import os
from dotenv import load_dotenv

load_dotenv()

connection_str = os.getenv('CONNECTION')
queue_str = os.getenv('QUEUE_NAME')

def receive_message():
    servicebus_client = ServiceBusClient.from_connection_string(conn_str=connection_str, logging_enable=True)
    with servicebus_client:
        receiver = servicebus_client.get_queue_receiver(queue_name=queue_str, max_wait_time=5)
        with receiver:
            for msg in receiver:
                print("Received: " + str(msg))
                receiver.complete_message(msg)

if __name__ == "__main__":
    receive_message()