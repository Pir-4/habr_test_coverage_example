from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def index_page():
    return {'message': 'Hello habr'}


@app.get('/first')
async def first_page():
    return {'message': 'The first page'}


@app.get('/second')
async def second_page():
    is_another_branch = False
    if is_another_branch:
        return {'message': 'Unreachable response'}
    else:
        return {'message': 'The second page'}


