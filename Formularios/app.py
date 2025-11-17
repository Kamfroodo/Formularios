from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        try:
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia_pct = int(request.form['asistencia'])

            promedio = (nota1 + nota2 + nota3) / 3

            promedio_aprobado = promedio >= 40
            asistencia_aprobada = asistencia_pct >= 75

            estado = "Reprobado"
            if promedio_aprobado and asistencia_aprobada:
                estado = "Aprobado"

            return render_template('ejercicio1.html',
                                   resultado_estado=estado,
                                   promedio_final=f"{promedio:.1f}",
                                   nota1_val=request.form.get('nota1'),
                                   nota2_val=request.form.get('nota2'),
                                   nota3_val=request.form.get('nota3'),
                                   asistencia_val=request.form.get('asistencia'))

        except ValueError:
            error_msg = "Error: Asegúrate de ingresar solo números válidos."
            return render_template('ejercicio1.html', error=error_msg,
                                   nota1_val=request.form.get('nota1'),
                                   nota2_val=request.form.get('nota2'),
                                   nota3_val=request.form.get('nota3'),
                                   asistencia_val=request.form.get('asistencia'))

    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_mas_largo = None
    longitud_maxima = 0

    if request.method == 'POST':
        nombre1 = request.form.get('nombre1', '').strip()
        nombre2 = request.form.get('nombre2', '').strip()
        nombre3 = request.form.get('nombre3', '').strip()

        nombres_con_longitud = [
            (nombre1, len(nombre1)),
            (nombre2, len(nombre2)),
            (nombre3, len(nombre3))
        ]

        for nombre, longitud in nombres_con_longitud:
            if longitud > longitud_maxima:
                longitud_maxima = longitud
                nombre_mas_largo = nombre

        if nombre_mas_largo and longitud_maxima > 0:
            resultado_nombre = f"El nombre con mayor cantidad de caracteres es : {nombre_mas_largo}"
            resultado_longitud = f"El nombre tiene : {longitud_maxima} caracteres"
        else:
            resultado_nombre = "Por favor, ingrese al menos un nombre."
            resultado_longitud = ""

        return render_template('ejercicio2.html',
                               resultado_nombre=resultado_nombre,
                               resultado_longitud=resultado_longitud,
                               nombre1_val=nombre1,
                               nombre2_val=nombre2,
                               nombre3_val=nombre3)

    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)