from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def import_data(cls, path):
        raise NotImplementedError("Método import_data não implementado")
