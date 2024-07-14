from fastapi import FastAPI
from rag_app.views import text_view, rag_view

app = FastAPI()

app.include_router(text_view.router, prefix="/texts")
app.include_router(rag_view.router, prefix="/rag")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
