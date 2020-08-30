from flask import Flask, render_template, request, redirect # added request
app = Flask(__name__)

@app.route('/')
def index():

    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    print("POST Form Submission")
    print(request.form)
    first_name_from_form = request.form['first_name']
    last_name_from_form = request.form['last_name']
    return render_template("show.html", name_on_template=first_name_from_form, last_name=last_name_from_form)




if __name__=="__main__":
    app.run(debug=True)