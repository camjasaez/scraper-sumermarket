import os
from datetime import datetime


def get_formatted_timestamp():
    """
    Returns a formatted timestamp string for use in filenames or metadata.

    Format: YYYY-MM-DD_HH-MM-SS

    Returns:
        str: Formatted timestamp string
    """
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def create_timestamped_filename(base_filename, extension='.json'):
    """
    Creates a filename with a timestamp.

    Args:
        base_filename (str): The base name of the file
        extension (str, optional): The file extension. Defaults to '.json'.

    Returns:
        str: A filename with the format {base_filename}_{timestamp}{extension}
    """
    timestamp = get_formatted_timestamp()
    return f"{base_filename}_{timestamp}{extension}"


def add_timestamp_to_json(json_data):
    """
    Adds a 'timestamp' field to the JSON data.

    Args:
        json_data (dict): The JSON data to modify

    Returns:
        dict: The modified JSON data with a 'timestamp' field
    """
    json_data['timestamp'] = get_formatted_timestamp()
    return json_data


def get_latest_file(directory, prefix):
    """
    Gets the latest file in a directory with a given prefix.

    Args:
        directory (str): The directory to search in
        prefix (str): The prefix of the files to search for

    Returns:
        str: The filename of the latest file, or None if no file is found
    """
    files = [f for f in os.listdir(directory) if f.startswith(prefix) and f.endswith('.json')]
    if not files:
        return None
    return max(files, key=lambda x: os.path.getctime(os.path.join(directory, x)))