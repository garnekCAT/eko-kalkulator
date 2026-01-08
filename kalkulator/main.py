# Import
from flask import Flask, render_template, request


app = Flask(__name__)

def result_calculate(size, lights, device):
    # Zmienne umożliwiające obliczenie poboru energii przez urządzenia
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5
    return size * home_coef + lights * light_coef + device * devices_coef

# Pierwsza strona
@app.route('/')
def index():
    return render_template('index.html')
# Druga strona
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html',
                            size=size
                           )

# Trzecia strona
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',
                            size = size,
                            lights = lights
                           )

# Obliczenia
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html',
                            result=result_calculate(int(size),
                                                    int(lights),
                                                    int(device)
                                                    )
                        )
# Formularz
@app.route('/form')
def form():
    return render_template('form.html')

# Wyniki formularza
@app.route('/submit', methods=['POST'])
def submit_form():
    # Zadeklaruj zmienne do gromadzenia danych
    name = request.form['name']
    email = request.form['email']
    date = request.form['date']
    adress = request.form['address']

    with open('form.txt', 'a', ) as f:
        f.write(email + '\n')
        f.write(name + '\n')
        f.write(date + '\n')
        f.write(adress + '\n')

    # Możesz zapisać swoje dane lub wysłać je e-mailem
    return render_template('form_result.html',
                           # Umieść tutaj zmienne
                           name=name,
                           email = email,
                           date = date,
                           adress = adress,
                           )


app.run(debug=True)