from distutils.log import error
from email import message
from flask import Flask,render_template,request, redirect
from pkg_resources import to_filename
import io

app = Flask(__name__)

@app.route("/index.html")
def Home():
    return render_template("index.html")

@app.route("/works.html")
def work():
    return render_template("works.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/components.html")
def components():
    return render_template("components.html")

@app.route("/text.html")
def text():
    return render_template('/text.html')

@app.route("/work.html")
def j():
    return render_template('/work.html')

@app.route("/about.html")
def about():
    return render_template('/about.html')

@app.route("/d.html")
def d():
    return render_template('/d.html')


def write_to_file(data):
    with io. open('data_base.txt',mode='a' ,encoding='utf8') as database:
       # with open('filename', 'w', encoding='utf-8') as f:
   # print(r['body'], file=f)
        email = data['email']
        message = data['message']
        subject = data['subject']
        file = database.write(f'n/{email},{subject},{message}')


@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
 if request.method == "POST":
            data = request.form.to_dict()
            write_to_file(data)
            return redirect('/d.html')
 
        
    

   

       
    
   

        
    






