from os import *
system("pip install flask")
from flask import Flask

# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Определяем маршрут для главной страницы
@app.route('/<m>')
def hello_world(m):
    return m

# Запускаем сервер
if __name__ == '__main__':
    app.run(host='0.0.0.0')
