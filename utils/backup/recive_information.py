import os


def receive_destination() -> str:
    destination = input('Enter the backup destination: ')

    while destination is None or not isinstance(destination, str):
        destination = input('Enter the backup destination: ')

    if not os.path.exists(destination):
        raise FileNotFoundError(f'The destination {destination} does not exist.')

    return destination


def receive_source() -> list:
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
        raise Exception(f'Error processing the backup source: {e}')

    return source_list
