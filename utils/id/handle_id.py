import json
import os
import logging


logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def check_file_and_folder() -> None:
    """
    Ensures that the 'core/id' folder and 'ids.json' file exist in the project directory.
    If the folder or file does not exist, they are created with an initial structure.
    Raises exceptions if there are issues creating the folder or file.
    """
    logging.info('Checking file and folder')
    project_path = os.getcwd()
    ids_folder = os.path.join(project_path, 'core', 'id')
    ids_file = os.path.join(ids_folder, 'ids.json')
    data = {
        "ids_in_use": []
    }

    if not os.path.exists(ids_folder):
        os.makedirs(ids_folder, exist_ok=True)

    if not os.path.exists(ids_file):
        try:
            with open(ids_file, 'w', encoding='utf-8') as file:
                if file is None:
                    raise ValueError('ids.json file is null')
                json.dump(data, file, ensure_ascii=False, indent=4)
        except json.JSONDecodeError:
            logging.error('Error decoding the JSON file')
            exit()
        except Exception as error:
            logging.error(f'Error creating the ids.json file: {error}')
            exit()


def load_ids() -> dict:
    """
    Loads the IDs from the 'ids.json' file located in 'core/id'.
    Ensures the file and folder exist before loading.
    Returns:
        dict: The content of the ids.json file as a dictionary.
    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file content is not a valid dictionary or cannot be decoded.
        Exception: For any other unexpected errors.
    """
    logging.info('Loading IDs')
    project_path = os.getcwd()
    ids_folder = os.path.join(project_path, 'core', 'id')
    ids_file = os.path.join(ids_folder, 'ids.json')
    check_file_and_folder()

    try:
        with open(ids_file, 'r', encoding='utf-8') as file:
            if file is None:
                raise ValueError('The ids.json file is null')
            ids_info = json.load(file)
            if ids_info is None:
                logging.error('ids_info is null')
                exit()
            if not isinstance(ids_info, dict):
                logging.error('ids_info is not a dictionary')
                exit()
            return ids_info
    except FileNotFoundError:
        logging.error('ids.json file not found')
        exit()
    except json.JSONDecodeError:
        logging.error('Error decoding the JSON file')
        exit()
    except Exception as error:
        logging.error('Unexpected error loading the ids: %s', error)
        exit()


def save_ids(data: dict) -> None:
    """
    Saves the provided dictionary to the 'ids.json' file in 'core/id'.
    Ensures the file and folder exist before saving.
    Args:
        data (dict): The data to be saved in the ids.json file.
    Raises:
        ValueError: If the provided data is None or not a dictionary.
        FileNotFoundError: If the file does not exist.
        Exception: For any other unexpected errors during saving.
    """
    logging.info('Saving IDs')
    project_path = os.getcwd()
    ids_folder = os.path.join(project_path, 'core', 'id')
    ids_file = os.path.join(ids_folder, 'ids.json')
    check_file_and_folder()

    if data is None:
        logging.error('Data is null')
        exit()

    if not isinstance(data, dict):
        logging.error('Data is not a dictionary')
        exit()

    try:
        with open(ids_file, 'w', encoding='utf-8') as file:
            if file is None:
                logging.error('The ids.json file is null')
                exit()
            json.dump(data, file, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        logging.error('ids.json file not found')
        exit()
    except json.JSONDecodeError:
        logging.error('Error decoding the JSON file')
        exit()
    except Exception as error:
        logging.error('Unexpected error saving the ids: %s', error)
        exit()
