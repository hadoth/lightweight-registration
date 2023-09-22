from typing import List

import strawberry
import lwreg
from lwreg.service.types import MoleculeEntry, RepresentationType
from lwreg.utils import defaultConfig


@strawberry.type
class Query:
    @strawberry.field
    def register_molecule(self, smiles: str) -> int:
        return lwreg.register(smiles=smiles, config=defaultConfig())

    @strawberry.field
    def query_molecule(self, smiles: str) -> List[int]:
        return lwreg.query(smiles=smiles, config=defaultConfig())

    @strawberry.field
    def retrieve_molecule(self, ids: List[int]) -> List[MoleculeEntry]:
        results = lwreg.retrieve(config=defaultConfig(), ids=ids)

        return [
            MoleculeEntry(result_tuple[0], result_tuple[1], RepresentationType.parse_representation_type(result_tuple[2])) for
            result_tuple in results
        ]
