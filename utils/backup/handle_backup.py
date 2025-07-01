import json
import os
import logging


logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def verify_file_and_folder(id: str) -> None:
    """
    Checks if the backup folder and the backup file for the given id exist.
    If the folder or file do not exist, they are created with default data.

    Args:
        id (str): The identifier for the backup file.

    Raises:
        Exception: If there is an error creating the backup file.
    """
    logging.info('Verify file and folder')
    project_path = os.getcwd()
    backup_folder = os.path.join(project_path, 'core', 'backup')
    id_file = os.path.join(backup_folder, f'{id}.json')
    data = {
        'id': None,
        'date': None,
        'time': None,
        'temporary_folder': None,
        'source': None,
        'destination': None
    }

    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder, exist_ok=True)
        logging.info('Backup information folder created successfully')

    if not os.path.exists(id_file):
        try:
            with open(id_file, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except json.JSONDecodeError:
            logging.error('Error decoding the JSON file')
            exit()
        except Exception as error:
            logging.error(f'Error creating the backup file: {error}')
            exit()

        logging.info(f'Backup file {id} created successfully')


def load_backup_information(id: str) -> None:
    """
    Loads the backup information from the JSON file for the given id.

    Args:
        id (str): The identifier for the backup file.

    Returns:
        dict: The backup information loaded from the file.

    Raises:
        FileNotFoundError: If the backup file does not exist.
        ValueError: If the file content is not a dictionary or cannot be decoded.
        Exception: For any other unexpected errors.
    """
    logging.info('Load backup information')
    project_path = os.getcwd()
    backup_folder = os.path.join(project_path, 'core', 'backup')
    id_file = os.path.join(backup_folder, f'{id}.json')
    verify_file_and_folder(id)

    try:
        with open(id_file, 'r', encoding='utf-8') as file:
            ids_info = json.load(file)
            if not isinstance(ids_info, dict):
                logging.error('ids_info is not a dictionary')
                exit()
            return ids_info
    except FileNotFoundError:
        logging.error('Backup file not found')
        exit()
    except json.JSONDecodeError:
        logging.error('Error decoding the JSON file')
        exit()
    except Exception as error:
        logging.error(f'Unexpected error loading the ids: {error}')
        exit()


def save_backup_information(id: str, data: dict):
    """
    Saves the backup information to the JSON file for the given id.

    Args:
        id (str): The identifier for the backup file.
        data (dict): The backup information to save.

    Raises:
        ValueError: If data is None or not a dictionary.
        Exception: For any other unexpected errors during saving.
    """
    logging.info('Save backup information')
    project_path = os.getcwd()
    backup_folder = os.path.join(project_path, 'core', 'backup')
    id_file = os.path.join(backup_folder, f'{id}.json')
    verify_file_and_folder(id)

    if data is None:
        logging.error('data is None')
        exit()
    
    if not isinstance(data, dict):
        logging.error('data is not a dictionary')
        exit()

    try:
        with open(id_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        logging.error('Backup file not found')
        exit()
    except json.JSONDecodeError:
        logging.error('Error decoding the JSON file')
        exit()
    except Exception as error:
        logging.error(f'Unexpected error saving the ids: {error}')
        exit()
