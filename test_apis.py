from flask import Flask, request, jsonify

app = Flask(__name__)

students = []
next_user_id=1

@app.route('/register_student', methods=['POST'])
def register_student():
    username=request.json['username']
    password=request.json['password']
    email=request.json['email'] 
    if not username or not password or not email:
        return jsonify({"error":"please fill all the feids "})
    global next_user_id
    student ={
        'user_id':next_user_id,
        'username':username,
        'password':password,
        'email':email
    }
    students.append(student)
    next_user_id +=1
    return jsonify({"message":"student register successfull"}),200

@app.route("/get_all_students", methods =['GET'])
def get_all_students():
    return jsonify(students)

@app.route("/update_student/<int:userid>", methods =['put'])
def update_student(userid):
    username=request.json['username']
    password=request.json['password']
    email=request.json['email']
    global students
    for student in students:
        if student['user_id'] == userid:
           student['username'] = username
           student['password'] = password
           student['email']= email
        return jsonify({"message":"student update successfull"}),200
    return jsonify({"error":"student not found"})

@app.route("/delete_student/<int:userid>", methods =['delete'])
def delete_student(userid):
    global students
    intil_students = len(students)
    students =[s for s in students if s['user_id'] != userid]
    if len(students) < intil_students:
        return ({"message":"student deleted successfull"}),200
    else:
        return ({"error":"student not found"})



if __name__ == __name__:
    app.run(debug = True)