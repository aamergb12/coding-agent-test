from flask import Flask, request, jsonify
from contact_manager import ContactManager
from email_service import EmailService
from database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
contact_manager = ContactManager()
email_service = EmailService()

@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify(contact_manager.get_all_contacts())

@app.route('/contacts', methods=['POST'])
def add_contact():
    data = request.get_json()
    return jsonify(contact_manager.add_contact(data))

@app.route('/contacts/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    data = request.get_json()
    return jsonify(contact_manager.update_contact(contact_id, data))

@app.route('/email/send', methods=['POST'])
def send_email():
    data = request.get_json()
    return jsonify(email_service.send_email(data))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)