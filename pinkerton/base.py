from enum import Enum


class EntityType(Enum):

    Person = 0
    Location = 1
    Organisation = 2
    Address = 3


class Entity:

    def __init__(self, type: EntityType, title: str, content: object):
        self.type = type
        self.title = title
        self.content = content

    @property
    def serialized(self):
        return {
            'title': self.title,
            'content': self.content,
        }
