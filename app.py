from flask import Flask,redirect,url_for,render_template,request
from forms import logFile
import csv,os

app=Flask(__name__)
app.config["SECRET_KEY"]='bdfbcdc502722bc56058y1d0'
@app.route('/',methods=['GET','POST'])
def home():
    form = logFile()
    if form.validate_on_submit():
        # Save the uploaded file to a temporary directory
        csv_filename = form.transaction_data.data.filename
        temp_path = os.path.join(app.instance_path, 'temp')
        os.makedirs(temp_path, exist_ok=True)
        csv_path = os.path.join(temp_path, csv_filename)
        form.transaction_data.data.save(csv_path)

        # Process the uploaded CSV file and read its data
        with open(csv_path, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                print(row)
        
    
       
    return render_template('index.html', form=form)

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)