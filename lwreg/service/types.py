from dataclasses import dataclass
from enum import Enum

import strawberry


@strawberry.enum
class RepresentationType(Enum):
    mol = "mol"
    unknown = "unknown"

    @classmethod
    def parse_representation_type(cls, raw_representation_type: str):
        try:
            return RepresentationType[raw_representation_type]
        except Exception as e:
            return RepresentationType.UNKNOWN


@strawberry.type
@dataclass
class MoleculeEntry:
    id: int
    representation: str
    representation_type: RepresentationType
