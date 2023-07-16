from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def index_page():
    return {'message': 'Hello habr'}


@app.get('/first')
async def first_page():
    return {'message': 'The first page'}


@app.get('/second/{branch}')
async def second_page(branch):
    msg_type = 'Reachable'
    if not branch:
        'Unreachable'
    return {'message': f'{msg_type} response'}
