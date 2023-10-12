from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy

app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)  # Initialize SQLAlchemy

# Import your models here
from server.models import Animal, Zookeeper, Enclosure

# Define routes and views here

@app.route('/animal/<int:id>', methods=['GET'])
def animal_by_id(id):
    # Retrieve the animal from the database based on the given ID
    animal = Animal.query.get(id)
    
    if not animal:
        return jsonify({'error': 'Animal not found'}), 404
    
    # Build a response containing the attributes of the animal
    response = {
        'animal ID': animal.id,
        'name': animal.name,
        'species': animal.species,
        'zookeeper': animal.zookeeper.name if animal.zookeeper else None,
        'enclosure': animal.enclosure.environment if animal.enclosure else None
    }
    
    return jsonify(response), 200

# Add similar routes and views for zookeeper_by_id and enclosure_by_id

if __name__ == '__main__':
    app.run(debug=True)


