from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datasets_ETL import get_max_duration, get_count_platform, get_listedin, get_actor

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
async def index():
    return '''
    <html>
    <head>
    </head>
    <body>
    <h1> Proyecto Data engineer </h1>
    <h2> ingrese a "/docs" para ver la documentación </h2>
    </body>
    </html>'''


@app.get('/get_max_duration({año}_{plataforma}_{Movie_o_TV_Show})')
async def duracion_maxima(año:int, plataforma:str, Movie_o_TV_Show:str):
    return get_max_duration(año, plataforma, Movie_o_TV_Show)


@app.get('/get_count_plataform({plataforma})')
async def cantidad_plataforma(plataforma:str):
    return get_count_platform(plataforma)


@app.get('/get_listedin({genero})')
async def genero_plataforma(genero:str):
    return get_listedin(genero)

@app.get('/get_actor({plataforma}_{anio})')
async def actor_repetido(plataforma:str, anio:int):
    return get_actor(plataforma, anio)