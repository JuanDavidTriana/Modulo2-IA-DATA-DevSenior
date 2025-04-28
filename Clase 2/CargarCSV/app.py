from flask import Flask, request, render_template
import pandas as pd

app= Flask(__name__)

@app.route('/', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        file= request.files['file']
        if file.filename.endswith('.csv'):
            df = pd.read_csv(file)
            resumen = {
                'filas' : df.shape[0],
                'columnas' : df.shape[1],
                'nombres_columnas' : list(df.columns),
            }
            return render_template('upload.html', resumen=resumen)
        else:
            return 'El archivo no es un CSV', 400 
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)


