import json
import os


def verify_file_and_folder(id) -> None:
    """
    Checks if the backup folder and the backup file for the given id exist.
    If the folder or file do not exist, they are created with default data.

    Args:
        id (str): The identifier for the backup file.

    Raises:
        Exception: If there is an error creating the backup file.
    """
    print('Verify file and folder')
    project_path = os.getcwd()
    backup_folder = os.path.join(project_path, 'core', 'backup')
    id_file = os.path.join(backup_folder, f'{id}.json')
    data = {
        'id': None,
        'timestamp': None,
        'temporary_folder': None,
        'source': None,
        'destination': None
    }

    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder, exist_ok=True)
        print('Backup information folder created successfully')

    if not os.path.exists(id_file):
        try:
            with open(id_file, 'w', encoding='utf-8') as file:
                json.dump(data, file)
        except json.JSONDecodeError:
            raise ValueError('Error decoding the JSON file')
        except Exception as error:
            raise Exception(f'Error creating the backup file: {error}')
        print(f'Backup file {id} created successfully')


def load_backup_information(id: str):
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
    print('Load backup information')
    project_path = os.getcwd()
    backup_folder = os.path.join(project_path, 'core', 'backup')
    id_file = os.path.join(backup_folder, f'{id}.json')
    verify_file_and_folder(id)

    try:
        with open(id_file, 'r', encoding='utf-8') as file:
            ids_info = json.load(file)
            if not isinstance(ids_info, dict):
                raise ValueError('ids_info is not a dictionary')
            return ids_info
    except FileNotFoundError:
        raise FileNotFoundError('Backup file not found')
    except json.JSONDecodeError:
        raise ValueError('Error decoding the JSON file')
    except Exception as error:
        raise Exception(f'Unexpected error loading the ids: {error}')


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
    print('Save backup information')
    project_path = os.getcwd()
    backup_folder = os.path.join(project_path, 'core', 'backup')
    id_file = os.path.join(backup_folder, f'{id}.json')
    verify_file_and_folder(id)

    if data is None:
        raise ValueError('data is None')
    
    if not isinstance(data, dict):
        raise ValueError('data is not a dictionary')

    try:
        os.makedirs(backup_folder, exist_ok=True)
        with open(id_file, 'w', encoding='utf-8') as file:
            json.dump(data, file)
    except FileNotFoundError:
        raise FileNotFoundError
    except json.JSONDecodeError:
        raise json.JSONDecodeError
    except Exception as error:
        raise Exception('Unexpected error saving the ids')
