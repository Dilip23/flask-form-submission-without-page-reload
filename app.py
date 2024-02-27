from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_folder='static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:SaiPrasanth@localhost:5432/flask-test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Leads(db.Model):
   id = db.Column(db.Integer, primary_key=True, autoincrement = True)
   f_name = db.Column(db.String(100), nullable=False)
   email = db.Column(db.String(100), nullable=False)
   
   def __repr__(self):
      return f'{self.f_name - self.email}' 



@app.route('/')
def home():
   return render_template('home.html')


@app.route('/submit', methods=['POST'])
def submit():
   name = request.form['name']
   email = request.form['email']
   print('*'*10)
   print(name,email)
   try:
    new_lead = Leads(
        f_name = name,
        email = email
    )
    db.session.add(new_lead)
    db.session.commit()
    print('Lead Captured!')
    return "Success!"
    # return jsonify({'message': 'Success! Data saved to database.'})
   except Exception as e:
      print(e)
      return str(e)



def create_tables():
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
   create_tables()
   app.run(debug=True)