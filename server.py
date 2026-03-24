from flask import Flask, request, redirect, url_for
import jinja2

app = Flask(__name__)
env = jinja2.Environment( loader=jinja2.FileSystemLoader('.'))

contacts = []

@app.route("/labelPage")
def labelPage():
    with open('LabelPage.html') as f:
        page = f.read()
    return page

@app.route("/testForm")
def testForm():
    tmp = env.get_template("testForm.html.j2")
    locations = ['Dublin','Dundalk','Drogheda','Newry']
    page = tmp.render(locations=locations, title="Add Contact")
    return page

@app.route("/addContact", methods=['POST'])
def addContact():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    location = request.form['location']
    contacts.insert(0, [firstname, lastname, location])

    return redirect(url_for('showContacts'))


@app.route("/showContacts")
def showContacts():
    # show contact list
    tmp = env.get_template("show_contacts.html.j2")
    page = tmp.render(title="Contacts", contacts=contacts)
    return page

if __name__ == '__main__': 
    app.run(host="127.0.0.1", port=4000)
