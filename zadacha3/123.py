from flask import Flask, url_for

app = Flask(__name__)


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <title>Пейзажи Марса</title>
    <style>
        .carousel-item img {{
            max-height: 500px;
            object-fit: cover;
        }}
    </style>
</head>
<body>
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-8 text-center">
                <h1>Пейзажи Марса</h1>

                <div id="marsCarousel" class="carousel slide mt-4" data-bs-ride="carousel">
                    <div class="carousel-inner">
                        <div class="carousel-item active">
                            <img src="{url_for('static', filename='img/mars1.jpg')}" class="d-block w-100" alt="Mars 1">
                        </div>
                        <div class="carousel-item">
                            <img src="{url_for('static', filename='img/mars2.jpg')}" class="d-block w-100" alt="Mars 2">
                        </div>
                        <div class="carousel-item">
                            <img src="{url_for('static', filename='img/mars3.jpg')}" class="d-block w-100"
                                 alt="Картинка 3 не загружена(СПЕЦИАЛЬНО ЧТОБЫ ВЫ ЭТО УВИДЕЛИ)">
                        </div>
                    </div>

                    <!-- Кнопки управления -->
                    <button class="carousel-control-prev" type="button" data-bs-target="#marsCarousel" data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Предыдущий</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#marsCarousel" data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Следующий</span>
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- ПРАВИЛЬНАЯ ССЫЛКА НА BOOTSTRAP JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
</body>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
