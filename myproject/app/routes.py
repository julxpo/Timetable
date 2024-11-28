#from app import app

#@app.route('/')
#def hello_world():
#    return "Всем привет!"

'''from flask import request
from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return 'Hello, World!'
    elif request.method == 'POST':
        return 'Hello, World! (POST-запрос)'
    else:
        return 'Неизвестный метод запроса' '''

from app import app
import psycopg

@app.route('/testdb')
def test_connection():
    try:
        con = psycopg.connect(host=app.config['DB_SERVER'],
                              user=app.config['DB_USER'],
                              password=app.config['DB_PASSWORD'],
                              dbname=app.config['DB_NAME'])
    except Exception as e:
        message = f"Ошибка подключения: {e}"
    else:
        message = "Подключение успешно"
    finally:
        if con:
            con.close()
        return message