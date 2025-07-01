import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def receive_destination() -> str:
    """
    Prompts the user to enter a backup destination path and validates its existence.

    Logs the process of receiving the backup destination. If the provided path does not exist,
    an error is logged and the program exits.

    Returns:
        str: The valid backup destination path entered by the user.
    """
    logging.info('Receive backup destination')
    destination = input('Enter the backup destination: ')

    while destination is None or not isinstance(destination, str):
        destination = input('Enter the backup destination: ')

    if not os.path.exists(destination):
        logging.error('The destination does not exist.')
        exit()

    return destination


def receive_source() -> list:
    """
    Prompts the user to enter one or more backup source paths, separated by commas.

    Returns:
        list: A list of backup source paths entered by the user.

    Logs:
        - Logs the start of the source receiving process.
        - Logs an error if there is an issue processing the input.

    Raises:
        Exits the program if an exception occurs while processing the input.
    """
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
