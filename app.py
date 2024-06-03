from flask import Flask, render_template, request
from math import sin, cos, tan, radians, degrees

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    angle = None
    result = None
    function = None
    unit = None
    precision = None

    if request.method == 'POST':
        try:
            angle = float(request.form.get('angle'))
            precision = int(request.form.get('precision'))
            function = request.form.get('function')
            unit = request.form.get('unit')

            if unit == 'градусы':
                angle = radians(angle)

            if function == 'sin':
                result = round(sin(angle), precision)
            elif function == 'cos':
                result = round(cos(angle), precision)
            elif function == 'tan':
                result = round(tan(angle), precision)
            else:
                error = "Некорректный выбор функции"

        except ValueError:
            error = "Некорректный ввод угла или точности"

    return render_template('index.html',
                           angle=angle,
                           result=result,
                           error=error,
                           function=function,
                           unit=unit,
                           precision=precision)


if __name__ == '__main__':
    app.run(debug=True)