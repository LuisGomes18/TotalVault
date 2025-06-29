import json
import os


def check_file_and_folder() -> None:
    """
    Ensures that the 'core/id' folder and 'ids.json' file exist in the project directory.
    If the folder or file does not exist, they are created with an initial structure.
    Raises exceptions if there are issues creating the folder or file.
    """
    print('Checking file and folder')
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
                json.dump(data, file)
        except json.JSONDecodeError:
            raise ValueError('Error decoding the JSON file')
        except Exception as error:
            raise Exception(f'Error creating the ids.json file: {error}')


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
    print('Loading IDs')
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
                raise ValueError('ids_info is null')
            if not isinstance(ids_info, dict):
                raise ValueError('ids_info is not a dictionary')
            return ids_info
    except FileNotFoundError:
        raise FileNotFoundError('ids.json file not found')
    except json.JSONDecodeError:
        raise ValueError('Error decoding the JSON file')
    except Exception as error:
        raise Exception(f'Unexpected error loading the ids: {error}')


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
    print('Saving IDs')
    project_path = os.getcwd()
    ids_folder = os.path.join(project_path, 'core', 'id')
    ids_file = os.path.join(ids_folder, 'ids.json')
    check_file_and_folder()

    if data is None:
        raise ValueError('data is null')

    if not isinstance(data, dict):
        raise ValueError('data is not a dictionary')

    try:
        with open(ids_file, 'w', encoding='utf-8') as file:
            if file is None:
                raise ValueError('The ids.json file is null')
            json.dump(data, file)
    except FileNotFoundError:
        raise FileNotFoundError('ids.json file not found')
    except json.JSONDecodeError:
        raise ValueError('Error decoding the JSON file')
    except Exception as error:
        raise Exception(f'Unexpected error saving the ids: {error}')
