import os


def receive_destination() -> str:
    """
    Prompts the user to input the backup destination path.

    Returns:
        str: The destination path for the backup.

    Raises:
        ValueError: If the destination is empty or None.
        TypeError: If the destination is not a string.
        FileNotFoundError: If the destination path does not exist.
    """
    destino = input('Enter the backup destination: ')

    if not destino:
        raise ValueError('The backup destination cannot be empty.')

    if destino is None:
        raise ValueError('The backup destination is null.')

    if not isinstance(destino, str):
        raise TypeError('The backup destination must be a string.')

    if not os.path.exists(destino):
        raise FileNotFoundError(f'The destination {destino} does not exist.')

    return destino


def receive_source() -> list:
    """
    Prompts the user to input the backup source paths, separated by commas.

    Returns:
        list: A list of source paths for the backup.

    Raises:
        ValueError: If the source input is empty, contains empty values, or does not exist.
        TypeError: If the source input is not a string.
        Exception: If an error occurs while processing the source input.
    """
    source = input('Enter the backup source(s), separated by commas: ')
    if not source:
        raise ValueError('The backup source cannot be empty.')

    if not isinstance(source, str):
        raise TypeError('The backup source must be a string.')

    if source is None:
        raise ValueError('The backup source is null.')

    source_list = []

    try:
        source_items = source.split(',')
        for item in source_items:
            item = item.strip()
            if not item:
                raise ValueError('The backup source contains an empty value.')
            if item is None:
                raise ValueError('The backup source contains a null value.')
            if not os.path.exists(item):
                raise ValueError(f'The source {item} does not exist.')
            source_list.append(item)
    except Exception as e:
        raise Exception(f'Error processing the backup source: {e}')

    return source_list
