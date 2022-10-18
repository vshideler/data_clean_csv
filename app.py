from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])

def upload():

    if request.method == 'POST':

        df = pd.read_csv(request.files.get('file'))

        old_shape = df.shape

        df = df.dropna()

        new_shape = df.shape

        return render_template('upload.html', shape=old_shape, new_shape=new_shape, dummy="Pav")

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
