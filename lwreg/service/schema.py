import strawberry
from strawberry.schema.config import StrawberryConfig

from lwreg.service.queries import Query

schema = strawberry.Schema(
    query=Query,
    config=StrawberryConfig(auto_camel_case=False),
)
