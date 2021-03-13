from flask import Flask, jsonify, request, render_template

from DataAccess.dbOp import DbOp
from Domain.intervention import Intervention
from Domain.technicien import Technicien
from Tools.tools import Tools

app = Flask(__name__)


@app.route('/api/intervention/add', methods=['POST'])
def add_intervention():

    """get json post"""
    new_inter = request.get_json(force=True)

    """create intervention object with received datas"""
    inter = Intervention()
    inter.createFromJson(new_inter)

    """update database"""
    inter.putInDb()

    return ("OK", {"Content-type": "application/plaintext"})


@app.route('/api/user/<username>')
def get_user_inters(username):

    mytech = Technicien(username)
    mytech.getAllInter()

    list = Tools.formatInterventions(mytech.interventions)

    return jsonify(list)

@app.route('/api/interventions')
def get_interventions():
    inter = Intervention()
    interventions = Tools.formatInterventions(inter.getAll())
    return jsonify(interventions)




if __name__ == '__main__':
    app.run()
