from flask import Flask, jsonify, request, Response
from DataAccess.accessDatabase import AccessDatabase

app = Flask(__name__)

@app.route('/api/interventions')
def get_interventions():
    #Retrieve intervention from database via DataAccess file
    dico = AccessDatabase.select_interventions()
    return jsonify(dico);

@app.route('/api/interventions/add', methods=['POST'])
def post_intervention():
    #add intervention to database via DataAccess file
    intervention = None
    AccessDatabase.insert_intervention(intervention)
    return Response("OK", status= 201, mimetype='application/Json')


if __name__ == '__main__':
    app.run()