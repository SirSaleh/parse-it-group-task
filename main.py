from fastapi import FastAPI
from rag_app.views import text_view # TODO add these in futre ,audio_view, image_view

app = FastAPI()

app.include_router(text_view.router, prefix="/text")

# TODO: Add theses in FUTURE
# app.include_router(audio_view.router, prefix="/audio")
# app.include_router(image_view.router, prefix="/image")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
