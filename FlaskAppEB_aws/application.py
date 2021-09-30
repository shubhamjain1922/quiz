from flask import Flask, render_template, request
from datetime import datetime
import pymysql
import pymysql.cursors
# import boto3
import time

# RDS
# client = boto3.client("rds")

instanceID = "myDBinstance"
username = "root"
password = "password123"
snapshotID = "myDBsnapshot"
DBname = "mySQLdb"
sgid = "sg-09cffbb37a1bae7ca"


# # # create instance
# # try:
# #     createDB_response = client.create_db_instance(
# #         DBName=DBname,
# #         DBInstanceIdentifier=instanceID,
# #         AllocatedStorage=10,
# #         Engine="mysql",
# #         DBInstanceClass="db.t2.micro",
# #         MasterUsername=username,
# #         MasterUserPassword=password,
# #         VpcSecurityGroupIds=[
# #             sgid,
# #         ],
# #         PubliclyAccessible=True,
# #     )
# # except Exception as e:
# #     print(e)

# # # wait till instance is ready
# # status = 0
# # for i in range(20):
# #     time.sleep(30)
# #     db_status = client.describe_db_instances(DBInstanceIdentifier=instanceID)[
# #         "DBInstances"
# #     ][0]["DBInstanceStatus"]
# #     if db_status == "available":
# #         print("instance is ready")
# #         status = 1
# #         break
# #     else:
# #         print(f"attempt {i}")

# # if status == 0:
# #     exit(1)

# db_endpoint = client.describe_db_instances(DBInstanceIdentifier=instanceID)["DBInstances"][0]['Endpoint']
# host=db_endpoint['Address']
# port=db_endpoint['Port']
# print(host)


host='mydbinstance.c8gxfyl0pspg.us-east-1.rds.amazonaws.com'

try:
        
    connection = pymysql.connect(host=host,
                                user=username,
                                password=password,
                                database=DBname,
                                cursorclass=pymysql.cursors.DictCursor)


    createTable = """CREATE TABLE `complains` (
            `id` INT PRIMARY KEY,
            `time` DATE,
            `userid` INT, 
            `text` VARCHAR(500)
        );"""

    with connection.cursor() as cursor:
        cursor.execute(createTable)
        connection.commit()

except Exception as e:
    print(e)


# APP
try:
    connection = pymysql.connect(host=host,
                                user=username,
                                password=password,
                                database=DBname,
                                cursorclass=pymysql.cursors.DictCursor)

except Exception as e:
    print(e)

insert ="""INSERT INTO `complains` (`id`,`time`,`userid`,`text`) VALUES
    (%s, %s, %s, %s);
    """
view = """SELECT * FROM `complains` ORDER BY `id` desc"""
getcount=""" select count(id) from `complains`;"""


application = app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("landing.html")

@app.route('/complain/', methods=["GET", "POST"])
def complain():
    
    try:
        if request.method == "POST":

            with connection.cursor() as cursor:
                cursor.execute(getcount)
                count = cursor.fetchone()['count(id)']
            connection.commit()

            count += 1
            print(request.form)
            id=request.form.get("uid")
            complain_text=request.form.get("complaint")

            with connection.cursor() as cursor:
                cursor.execute(insert, (count, datetime.now().strftime("%Y-%m-%d"), id, complain_text))
            connection.commit()
    except Exception as e:
        print(e)
    

    return render_template("complain.html")

@app.route('/team/', methods=["GET", "POST"])
def team():
    try:
        with connection.cursor() as cursor:
            cursor.execute(view)
            result = cursor.fetchall()
    except Exception as e:
        print(e)

    return render_template('team.jinja2', coms=result)

if __name__ == '__main__':
    app.run()

