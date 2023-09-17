from enum import Enum


class address_choices(Enum):
    Pathankot="pathankot"
    Jalandhar="Jalandhar"
    Ludhiana="ludhiana"

    @classmethod
    def demo(cls):
        return ((i.name,i.value) for i in address_choices)