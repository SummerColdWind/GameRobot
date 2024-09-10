from abc import ABC, abstractmethod


class PluginInterface(ABC):
    def __init__(self, robot):
        self.robot = robot

    @abstractmethod
    def __repr__(self):
        """ Returns the text for the plugin description """
        raise NotImplementedError

    @abstractmethod
    def perform(self, command):
        raise NotImplementedError
