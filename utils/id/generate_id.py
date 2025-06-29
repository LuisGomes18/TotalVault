from utils.id.handle_id import load_ids, save_ids
import uuid


def generate_id(max_char: int = None | 8) -> str:
    """
    Generates a unique ID string of a specified maximum length.
    This function attempts to generate a unique ID that is not currently in use,
    using a truncated UUID. The length of the generated ID can be specified via
    the `max_char` parameter. If not provided, the default length is 8 characters.
    Args:
        max_char (int, optional): The maximum number of characters for the generated ID.
            Defaults to 8.
    Returns:
        str: A unique ID string of up to `max_char` characters.
    Raises:
        Exception: If there is an error loading IDs or generating a unique ID.
    """

    try:
        if max_char is None:
            max_char = 8

        IDS = load_ids()
        if IDS is None:
            raise ValueError('IDS is None')

        ids_in_use = IDS.get('ids_in_use')
        if ids_in_use is None:
            raise ValueError('IDS.get("ids_in_use") is None')

        while True:
            id = str(uuid.uuid4())[:max_char].replace('-', '')

            if id not in ids_in_use:
                return id
    except Exception as error:
        raise Exception(f'Error generating ID: {error}')
