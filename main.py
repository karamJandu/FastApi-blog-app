from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/blog")
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from the database'}
    else:
        return {'data': f'{limit} blogs from the database'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id: int, limit=10):
    return {'data': ['1', '2']}


@app.get('/about')
def about():
    return {'data': 'about page'}


blogs = []

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]



@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog is created with title {blog.title}, body {blog.body}, published {blog.published}'}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
