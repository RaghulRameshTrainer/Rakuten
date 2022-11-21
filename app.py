from flask import Flask,jsonify,request
app=Flask(__name__)

employee=[
    {
        'name':'Raghul Ramesh',
        'tech':[
                   {
                       'name':'Python',
                       'exp':17
                   }
               ]
    },
    {
        'name':'Malini',
        'tech':[
            {
                'name':'Java',
                'exp':11
            }
        ]
    }
    ]
@app.route('/')
def home():
    return "<h1>Hello, The flask application is running successfully</h1>"

@app.route('/emp/<string:name>')
def get_employee(name):
    for e in employee:
        if(e['name']==name):
            return jsonify(e['name'])
    return jsonify({'message':'Employee not found'})

@app.route('/emp/<string:name>/tech')
def get_employee_tech(name):
    for emp in employee:
        if emp['name']==name:
            return jsonify(emp['tech'])
    return jsonify({'message':'Tech not found'})

@app.route('/emp',methods=['POST'])
def add_employee():
    req_data=request.get_json()
    new_emp={
        'name':req_data['name'],
        'tech':req_data['tech']
    }
    employee.append(new_emp)
    return jsonify(new_emp)

@app.route('/emp/<string:name>',methods=["DELETE"])
def delete_employee(name):
    i=0
    for e in employee:
        if e['name']==name:
            employee.pop(i)
            return jsonify({"message":"employee record has been deleted"})
        i=i+1
    return jsonify({'message':'Employee record is not present!'})


if __name__=='__main__':
    app.run(port=5000)

