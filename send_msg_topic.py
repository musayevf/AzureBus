from azure.servicebus import ServiceBusClient, ServiceBusMessage
import os
from dotenv import load_dotenv

load_dotenv()
connection_str= os.getenv('TOPIC_CONNECTION')
topic_name= os.getenv('TOPIC_NAME')

def send_message_to_topic():
    servicebus_client = ServiceBusClient.from_connection_string(conn_str=connection_str, logging_enable=True)
    with servicebus_client:
        sender = servicebus_client.get_topic_sender(topic_name=topic_name)
        with sender:
            message = ServiceBusMessage("Azure Service BUS Topic")
            sender.send_messages(message)
            print("Message sent to topic")

if __name__ == "__main__":
    send_message_to_topic()
