import datetime


def get_date():
    """Returns the current date in the format of dd/mm/yyyy

    :return: str
    """
    return datetime.datetime.now().strftime("%d/%m/%Y")


def get_time():
    """Returns the current time in the format of hh:mm:ss

    :return: str
    """
    return datetime.datetime.now().strftime("%H:%M:%S")


def format_dict(dictionary):
    return None


def color_string(string):
    """Colors a string.

    :param string: The string to color.

    :type string: str

    :return: str
    """
    return string
