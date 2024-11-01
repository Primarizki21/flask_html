import csv
from flask import Flask, render_template, request, redirect, url_for, jsonify


app = Flask(__name__)

def fibonacci1(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Halaman utama (Home)
@app.route('/')
def home():
    return render_template('home.html')

# Halaman CV
@app.route('/cv')
def cv():
    return render_template('cv.html')

# Halaman Portofolio
@app.route('/portofolio')
def portofolio():
    return render_template('portofolio.html')

# Halaman Biodata
@app.route('/biodata')
def biodata():
    return render_template('biodata.html')

# Halaman Fibonacci (Input angka dan hasil Fibonacci)
@app.route('/fibonacci', methods=['GET', 'POST'])
def fibonacci():
    result = None
    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            result = fibonacci1(number)
        except ValueError:
            result = "Please enter a valid integer."
    return render_template('fibonacci.html', result=result)

@app.route('/csvtojson')
def csvtojson():
    return render_template('csvtojson.html')
# Halaman untuk menampilkan CSV dalam format JSON
@app.route('/data-json', methods=['GET', 'POST'])
def data_json():
    data = []
    # file_path = 'templates/datapribadi.csv'  # Ensure this path is correct
    file = request.files['fileInput']  # Ensure this path is correct

    # Check if file exists before attempting to read
    # if not os.path.isfile(file_path):
    #     return jsonify({"error": "File not found"}), 404

    try:
        # Read the CSV data
        file_stream = file.stream  # Access the file stream
        reader = csv.DictReader(file_stream.read().decode('utf-8').splitlines())
        for row in reader:
            data.append(row)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(data)
# Halaman Form dengan POST Method
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        return render_template('result.html', name=name, age=age)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)