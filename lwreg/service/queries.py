import strawberry
import lwreg
from lwreg.utils import defaultConfig


@strawberry.type
class Query:
    @strawberry.field
    def register_molecule(self, smiles: str) -> int:
        return lwreg.register(smiles=smiles, config=defaultConfig())
