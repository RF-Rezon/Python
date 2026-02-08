from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome to the page.'

##-------------------------------------------------

@app.route('/index')
def html_page():
    return render_template("index.html")

##-------------------------------------------------

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['user_name']  ## html e name attribute dhote
        return f'Hei {name}.'
    return render_template("form.html")

##-------------------------------------------------

@app.route('/success/<int:id>')
def success(id):
    res=""

    if id <= 40:
        res = 'Too low.'
    if id > 40:
        res = 'Good.'
    
    return render_template('success.html', result=res, point=id)

## -------------------------------------------------

@app.route('/results',methods =['POST', 'GET'])
def exam_results():
    if request.method == 'POST':
        sub1Marks = int(request.form['sub1'])
        sub2Marks = int(request.form['sub2'])
        sub3Marks = int(request.form['sub3'])

        avg_marks = (sub1Marks + sub2Marks + sub3Marks)/3
    else:
        return render_template('exam_results.html')

    return redirect(url_for('success',id=avg_marks))    

if __name__ == '__main__':
    app.run(debug=True)