from flask import Flask ,request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

employee =[ {
    "name":"Ajinkya",
    "salary":"10000"
 }]


@app.route('/employee',methods=['GET'])
def get_employee():
    return jsonify(employee)
  
@app.route('/addemployee', methods=['POST'])
def add_employee():

    try:
        data = request.get_json(force=True)
    except BadRequest:
        return jsonify({"error": "Request body must contain valid JSON."}), 400

    if not isinstance(data, dict):
        return jsonify({"error": "JSON body must be an object."}), 400

    employee.append(data)

    return jsonify(
        {
            "msg":"Employee added sucessfully",
            "employee":data
        }
    )

if __name__ == '__main__':
    app.run(debug = True)
