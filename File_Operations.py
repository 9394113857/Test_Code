import os
from datetime import datetime
from urllib import request

from flask import Flask, request, make_response, json, jsonify
from flask_mysqldb import MySQL

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'media/files'  # 'media/images'
ALLOWED_EXTENSIONS = (['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

app.config['MYSQL_HOST'] = '35.213.140.165'
app.config['MYSQL_USER'] = 'uwgwdvoi7jwmp'
app.config['MYSQL_PASSWORD'] = 'Clinicalfirst@123'
app.config['MYSQL_DB'] = 'dbim4u0mfuramq'
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

mysql = MySQL(app)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/file', methods=['POST'])
def index():
    now = datetime.now()
    if request.method == 'POST':
        userDetails = None
        path = request.form['user_folder_path + filename']
        mail_id = request.form['mail_id']
        if request.files['file']:
            userDetails = request.files['file']
        # else:
        #     userDetails = users(request.form)
        if userDetails and allowed_file(userDetails.filename):
            filename = secure_filename(userDetails.filename)
            user_folder_path = app.config['UPLOAD_FOLDER'] + '/pics/'
            if not os.path.exists(user_folder_path):
                os.makedirs(user_folder_path)
            userDetails.save(os.path.join(user_folder_path, filename))
            try:
                cursor = mysql.connection.cursor()
                cursor.execute('INSERT INTO Images(file_name,mail_id,uploaded_on) VALUES(%s,%s,%s)',
                               (user_folder_path + filename, mail_id, now))
                mysql.connection.commit()
                cursor.close()
            except Exception as e:
                print(e)
                return "Unable to insert image metadata to db"
            return "File uploaded successfully."


# all_rows
@app.route("/all_rows", methods=['GET'])
def all_rows():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM Images')
    data = cursor.fetchall()
    return make_response(jsonify({"Data": data}))


# Single id
@app.route("/row/<id>", methods=['GET'])
def row_id(id):
    Id = id
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM Images where Id =' + Id)
    data = cursor.fetchone()
    return make_response(jsonify({"Data": data}))


# Update
@app.route("/row/update/<id>", methods=['PUT'])
def update_id(id):
    emaild = request.json["email"]
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE Images set mail_id = %s where Id = %s', (emaild,id))
    mysql.connection.commit()
    return "File Updated Successfully"


# Delete
@app.route("/row/delete/<Id>", methods=["DELETE"])
def delete_id(Id):
    cursor = mysql.connection.cursor()
    cursor.execute("delete from Images where Id = %s", (Id,))
    mysql.connection.commit()
    return "File Deleted Successfully"


if __name__ == "__main__":
    app.run(debug=True)
