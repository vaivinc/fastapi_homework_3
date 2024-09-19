import uvicorn
import httpx
from fastapi import FastAPI

app = FastAPI()


@app.get("/users/")
async def get_users():
    url = 'https://jsonplaceholder.typicode.com/users/'
    async with httpx.AsyncClient() as ac:
        response = await ac.get(url)
        return response.status_code, response.json()


@app.post("/users/create/")
async def users_post(title: str, body: str):
    url = 'https://jsonplaceholder.typicode.com/users'
    userID = 1

    async with httpx.AsyncClient() as ac:
        response = await ac.post(url,
                                 json={
                                     "title": title,
                                     "body": body,
                                     "userID": userID
                                 })
        return response.status_code, response.json()


@app.delete("/users/delete/")
async def users_delete():
    url = 'https://jsonplaceholder.typicode.com/users'

    async with httpx.AsyncClient() as ac:
        response = await ac.delete(url)
        return response.status_code, response.json()


if __name__ == '__main__':
    uvicorn.run("__main__:app", reload=True)