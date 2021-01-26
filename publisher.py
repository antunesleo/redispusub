from time import sleep
from typing import List

import redis

MESSAGES_CHANNEL = 'messages'

MESSAGES_DATASET = [
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    'Etiam condimentum in massa at efficitur.',
    'Mauris ligula odio, tristique sit amet fringilla in, mattis nec neque.',
    'Curabitur ultricies, velit consectetur pellentesque varius.',
    'Vivamus suscipit lacus a est lacinia vulputate et eu massa.',
    'Quisque ac magna ligula. In eu diam magna.',
    'Nam condimentum ultrices purus, vel rutrum diam tempor sed.',
    'Quisque non ornare enim.',
    'Maecenas vel lectus eu leo finibus feugiat.'
    'Praesent interdum ullamcorper libero.',
    'Velit consectetur pellentesque ipsum dolor lorem.'
]

redis_conn = redis.Redis()


def publish_messages(channel: str, messages: List[str], delay: int):
    """Publishes a collection of messages into a channel

    :param channel: the name of the channel to put the messages
    :param messages: list of string messages to be sent
    :param delay: number of seconds do wait between messages
    """
    print('----Starting to send the messages----')
    for index, message in enumerate(messages):
        redis_conn.publish(channel, message)
        print(f'Sent {index+1} of {len(messages)} messages')
        sleep(delay)

    print('------------Messages Sent------------')


if __name__ == '__main__':
    publish_messages(MESSAGES_CHANNEL, MESSAGES_DATASET, 2)
