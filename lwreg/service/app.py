import uvicorn
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from lwreg.service.schema import schema


app = FastAPI(
    title="Lightweight Registration Service",
    description="Service used to register molecules"
)
app.include_router(GraphQLRouter(schema), prefix="/graphql")

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        log_level="info",
        app_dir="src",
        reload=True,
    )
