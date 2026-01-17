from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        try:
            nota1 = int(request.form['nota1'])
            nota2 = int(request.form['nota2'])
            nota3 = int(request.form['nota3'])
            asistencia = int(request.form['asistencia'])

            # Validaciones (abortar si no cumplen rangos, criterio 5: abortar conexiones)
            if not (10 <= nota1 <= 70 and 10 <= nota2 <= 70 and 10 <= nota3 <= 70 and 0 <= asistencia <= 100):
                abort(400, description="Valores fuera de rango")

            promedio = round((nota1 + nota2 + nota3) / 3,1) # Redondea a 1 Decimal
            estado = "Aprobado" if promedio >= 40 and asistencia >= 75 else "Reprobado"

            return render_template('ejercicio1.html', promedio=promedio, estado=estado)
        except ValueError:
            abort(400, description="Entrada inválida")

    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1'].strip()
        nombre2 = request.form['nombre2'].strip()
        nombre3 = request.form['nombre3'].strip()

        # Validar que sean diferentes (manipulación en memoria, criterio 10)
        if len(set([nombre1, nombre2, nombre3])) != 3:
            abort(400, description="Los nombres deben ser diferentes")

        nombres = [nombre1, nombre2, nombre3]
        nombre_largo = max(nombres, key=len)
        longitud = len(nombre_largo)

        return render_template('ejercicio2.html', nombre_largo=nombre_largo, longitud=longitud)

    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)