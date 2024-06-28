from azure.servicebus import ServiceBusClient
import os
from dotenv import load_dotenv

load_dotenv()
connection_str= os.getenv('TOPIC_CONNECTION')
topic_name= os.getenv('TOPIC_NAME')
sub_name = os.getenv('SUBSCRIPTION_NAME')

def receive_message_from_subscription():
    servicebus_client = ServiceBusClient.from_connection_string(conn_str=connection_str, logging_enable=True)
    with servicebus_client:
        receiver = servicebus_client.get_subscription_receiver(
            topic_name=topic_name,
            subscription_name=sub_name,
            max_wait_time=5
        )
        with receiver:
            for msg in receiver:
                print("Received: " + str(msg))
                receiver.complete_message(msg)

if __name__ == "__main__":
    receive_message_from_subscription()
