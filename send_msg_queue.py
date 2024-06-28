from azure.servicebus import ServiceBusClient, ServiceBusMessage
import os
from dotenv import load_dotenv

load_dotenv()

connection_str = os.getenv('CONNECTION')
queue_str = os.getenv('QUEUE_NAME')

def send_message():
    servicebus_client = ServiceBusClient.from_connection_string(conn_str=connection_str, logging_enable=True)
    with servicebus_client:
        sender = servicebus_client.get_queue_sender(queue_name=queue_str)
        with sender:
            message = ServiceBusMessage("Azure Service BUS queue")
            sender.send_messages(message)
            print("Message sent")

if __name__ == "__main__":
    send_message()