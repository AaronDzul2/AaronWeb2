from flask import Flask, render_template, request, redirect, url_for
import pymysql
from conexion import conectar_db

app = Flask(__name__)

db = conectar_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    mensaje = request.args.get('mensaje')
    return render_template('login.html', mensaje=mensaje)


@app.route('/Validacion', methods=['POST'])
def Validacion():
    correo = request.form.get('correo')
    contraseña = request.form.get('password')

    # Verificar si se proporcionaron el correo y la contraseña
    if not correo or not contraseña:
        return redirect(url_for('login', mensaje='Debes proporcionar correo y contraseña'))

    # Consultar la base de datos para verificar las credenciales
    cursor = db.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE correo=%s AND password=%s", (correo, contraseña))
    usuario = cursor.fetchone()

    # Si se encontró un usuario con las credenciales proporcionadas, redirigir a la página de perfil
    if usuario:
        return "Bienvenido"
    else:
        # Si las credenciales no son válidas, redirigir a la página de inicio de sesión con un mensaje de error
        return redirect(url_for('login', mensaje='Credenciales no válidas'))


if __name__ == '__main__':
    app.run(debug=True)
