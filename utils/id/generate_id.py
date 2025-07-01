from utils.id.load_ids import load_ids
import uuid
import logging



logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def generate_id(max_char: int = None) -> str:
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
    logging.info('Generating a new ID')
    try:
        if max_char is None:
            max_char = 8
            logging.info('max_char not provided. Using default value: 8.')

        IDS = load_ids()
        logging.info('IDs loaded successfully.')
        if IDS is None:
            logging.error('IDS is None.')
            raise ValueError('IDS is None')

        ids_in_use = IDS.get('ids_in_use')
        if ids_in_use is None:
            logging.error('IDS.get("ids_in_use") is None.')
            raise ValueError('IDS.get("ids_in_use") is None')

        while True:
            generated_id = str(uuid.uuid4())[:max_char].replace('-', '')
            logging.info('Generated ID with sucess')

            if generated_id not in ids_in_use:
                logging.info('Generated ID is not in use. Returning the ID.')
                return generated_id
            else:
                logging.info('ID is already in use. Trying again.')
    except Exception as error:
        logging.error('Error generating ID: %s', error)
        exit()
