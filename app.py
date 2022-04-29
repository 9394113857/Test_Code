import logging

import MySQLdb
from flask import request, Flask, session, jsonify, make_response
from flask_mysqldb import MySQL
from marshmallow import ValidationError
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# live database
app.config['MYSQL_HOST'] = '35.213.140.165'
app.config['MYSQL_USER'] = 'uwgwdvoi7jwmp'
app.config['MYSQL_PASSWORD'] = 'Clinicalfirst@123'
app.config['MYSQL_DB'] = 'dbim4u0mfuramq'
app.config['SECRET_KEY'] = 'secret-key'

mysql = MySQL(app)


# New User:
@app.route('/new/user', methods=['POST'])
def PATIENT_PERSONAL_DETAILS():
    if 'username' in request.json and 'email' in request.json \
            and 'phone' in request.json and 'password' in request.json:
        # Variables:
        request_data = request.json
        username = request_data['username']
        email = request_data['email']
        phone = request_data['phone']
        password = request_data['password']
        hassedpassword = generate_password_hash(password)
        # UserId Pattern for Insert Operation:-
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT PATIENT_ID FROM PATIENT_PERSONAL_DETAILS")
        last_user_id = cursor.rowcount
        print('----------------------------------')
        print("Last Inserted ID is: " + str(last_user_id))
        pattern = 'PA000'  # pattern = ooo
        last_user_id += 1
        # add_value = 00
        # pattern += 1 # pattern incrementing always by 1:-
        user_id = pattern + str(last_user_id)  # pass 'user_id' value in place holder exactly
        # Cursor:-
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM PATIENT_PERSONAL_DETAILS WHERE PATIENT_MAIL_ID = %s OR PATIENT_PHONE_NUMBER = %s',
                       (email, phone))
        account = cursor.fetchone()
        if account and account[3] == email:
            return 'Your Email already exist please enter new Email !', 400
        elif account and account[4] == phone:
            return "Your Phone number is duplicate please enter new number!!!", 400
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "insert into PATIENT_PERSONAL_DETAILS(PATIENT_ID, PATIENT_NAME, PATIENT_MAIL_ID, PATIENT_PHONE_NUMBER, PATIENT_PASSWORD) VALUES(%s, %s, %s, %s, %s)",
                (user_id, username, email, phone, hassedpassword))
            mysql.connection.commit()
            logging.info("successfully registered")
            # return fun("successfully inserted", args, *kwargs), 201
            return "User Registered Successfully", 200
        except ValidationError as e:
            # logTo_database("/user/insert", "user_signup", e, 401)
            return (e.messages), 400
    return "Invalid input", 200


# User Login:-
@app.route('/user/login', methods=["POST"])
def login():
    if 'email' in request.json and 'password' in request.json:
        email = request.json["email"]
        logging.info('Admin logged in')
        pw = request.json["password"]
        logging.warning('Watch out!')
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("select * from PATIENT_PERSONAL_DETAILS WHERE (PATIENT_MAIL_ID = %s )",
                    (email,))  # PATIENT_PERSONAL_DETAILS, PATIENT_SIGNUP
        details = cur.fetchone()
        if details is None:
            return ({"message": "No details"}), 401
        # if details and details["PATIENT_MAIL_ID"]!= email:
        #     return "invalid mailid"
        hashed_password = details["PATIENT_PASSWORD"]
        password_match = check_password_hash(hashed_password, pw)
        if password_match:
            session['loggedin'] = True
            session['PATIENT_ID'] = details['PATIENT_ID']
            return "successfully login"
        else:
            logging.error("Invalid credentials")
        return ({"Error": "invalid credentials"}), 401
    return "Insufficient parameters", 400


# User Logout:-
@app.route('/user/logout', methods=['POST'])
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('PATIENT_ID', None)
    return "User Loggedout Successfully !!!"


# AMB_BOOKING
@app.route('/amb/booking', methods=["POST"])
def book():
    if 'loggedin' in session:
        if 'situation_type' in request.json and 'cause_type' in request.json \
                and 'amb_type' in request.json and "price" in request.json and "advance_type_or_basic" in request.json:
            patient_id = session['PATIENT_ID']

            situation_type = request.json["situation_type"]
            amb_type = request.json["amb_type"]
            advance_name_or_basic = request.json["advance_type_or_basic"]
            cause = request.json["cause_type"]
            price = request.json["price"]

            try:
                cur = mysql.connection.cursor()
                cur.execute("select SITUATION_ID from AMB_SITUATIONS where (SITUATION_TYPE = %s)", (situation_type,))
                data1 = cur.fetchone()
                if data1 is None:
                    return "No details in account"
                cur = mysql.connection.cursor()
                cur.execute("select AMB_TYPE_ID from AMB_AMBULANCE_TYPES where (AMB_TYPE = %s)", (amb_type,))
                data2 = cur.fetchone()
                if data2 is None:
                    return "No data in your account"
                cur = mysql.connection.cursor()
                cur.execute("select BASIC_TYPE_ID from AMB_BASIC_TYPES where (BASIC_TYPE_NAME = %s)",
                            (advance_name_or_basic,))
                data3 = cur.fetchone()
                if data3 is None:
                    cur = mysql.connection.cursor()
                    cur.execute("select ADVANCED_TYPE_ID from AMB_ADVANCED_TYPES where (ADVANCED_TYPE_NAME = %s)",
                                (advance_name_or_basic,))
                    data3 = cur.fetchone()
                    if data3 is None:
                        return "No data in your account"
                cur = mysql.connection.cursor()
                cur.execute("select CAUSE_ID from AMB_CAUSES where (CAUSE_TYPE = %s)", (cause,))
                data5 = cur.fetchone()
                if data5 is None:
                    return "No data in your account"
                cur = mysql.connection.cursor()
                cur.execute(
                    "insert into AMB_BOOKING(PATIENT_ID,SITUATION_ID, AMB_TYPE_ID, BASIC_OR_ADVANCE, CAUSE_ID, PRICE)"
                    "values(%s,%s,%s,%s,%s,%s)", (patient_id, data1, data2, data3, data5, price))
                mysql.connection.commit()
                return "successfully inserted", 200
            except ValidationError as e:
                print(e)
            return jsonify(e.messages)
        return "invalid parameters"
    return "User not loggedin, please login first"


# /get/all
@app.route("/get/all", methods=['GET'])
def get_all():
    if "loggedin" in session:
        cursor = mysql.connection.cursor()
        cursor.execute(
            'SELECT PATIENT_ID,PATIENT_NAME,PATIENT_MAIL_ID,PATIENT_PHONE_NUMBER FROM PATIENT_PERSONAL_DETAILS')
        data = cursor.fetchall()
        return make_response(jsonify({"Data": data}))
    return "User not loggedin, please login first"


# /get/id
@app.route("/get/<id>", methods=['GET'])
def row_id(id):
    if "loggedin" in session:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM PATIENT_PERSONAL_DETAILS where ID =' + id)
        data = cursor.fetchone()
        return make_response(jsonify({"Data": data}))
    return "User not loggedin, please login first"


# Update
@app.route("/user/update/<id>", methods=['PUT'])
def update_id(id):
    user_name = request.json["user_name"]
    user_mail = request.json["user_mail"]
    user_number = request.json["user_number"]
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE PATIENT_PERSONAL_DETAILS set PATIENT_NAME = %s, PATIENT_MAIL_ID = %s, PATIENT_PHONE_NUMBER = %s where ID = %s', (user_name, user_mail, user_number, id))
    mysql.connection.commit()
    return "User Updated Successfully"


# Delete
@app.route("/user/delete/<Id>", methods=["DELETE"])
def delete_id(Id):
    cursor = mysql.connection.cursor()
    cursor.execute("delete from PATIENT_PERSONAL_DETAILS where ID = %s", (Id,))
    mysql.connection.commit()
    return "User Deleted Successfully"


# MAIN app To Run the Flask Script:-
if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host="0.0.0.0", port=8080, debug=True)
