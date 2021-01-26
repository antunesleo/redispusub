from time import sleep
from typing import List

import redis

MESSAGES_CHANNEL = 'messages'

def handle_message(message):
    print(f'I have received the message: {message}')

redis_conn = redis.Redis()
pubsub_inst = redis_conn.pubsub(ignore_subscribe_messages=True)
pubsub_inst.subscribe(**{MESSAGES_CHANNEL: handle_message})


def listen_to_publishings():
    while True:
        pubsub_inst.get_message()
        sleep(0.001)


if __name__ == '__main__':
    listen_to_publishings()
