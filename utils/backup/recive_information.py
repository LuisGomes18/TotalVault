import os
import logging

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def receive_destination() -> str:
    logging.info('Receive backup destination')
    destination = input('Enter the backup destination: ')

    while destination is None or not isinstance(destination, str):
        destination = input('Enter the backup destination: ')

    if not os.path.exists(destination):
        logging.error('The destination does not exist.')
        exit()

    return destination


def receive_source() -> list:
    logging.info('Receive backup source')
    source = input('Enter the backup source(s), separated by commas: ')

    while source is None or not isinstance(source, str):
        source = input('Enter the backup source(s), separated by commas: ')

    source_list = []

    try:
        source_items = source.split(',')
        for item in source_items:
            item = item.strip()
            source_list.append(item)

    except Exception as e:
        logging.error('Error processing the backup source: %s', e)
        exit()

    return source_list
