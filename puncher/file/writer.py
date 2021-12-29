import time
import yaml


class Section:
    def __init__(self, name: str = None, content: list = None):
        """

        :param name: The name of the section.
        :param content: The content of the section. Default is a null list
        """
        if content is None:
            content = list()
        if name is None:
            name = "new_section_" + str(round(time.time() * 1000))
        self.name = name
        self.content = content


class Writer:
    def __init__(self):
        pass

    @staticmethod
    def save(data: Section) -> bool:
        """

        :param data: Section data to be saved
        :return: Whether the save succeeds.
        """
        pass
