
import connector as cn
import time
from sense_hat import SenseHat

def GetData ():
    sense = SenseHat()
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    return (temperature, humidity, pressure)


def ExecuteToDB (temperature, humidity, pressure):
    thisConn = cn.dbconnect()
    myCursor = thisConn.cursor()
    q="""
    INSERT INTO hatdata (Temperature, Humidity, BarometricPressure)
    VALUES ('"""+ str(temperature) + """', '"""+ str(humidity)+"""', '""" + str(pressure) + """');
    """
    myCursor.execute(q)
    time.sleep(10)
    thisConn.commit()

# def ExecuteToWeb ():
#     thisConn = cn.dbconnect()
#     myCursor = thisConn.cursor()
#     data=""" SELECT Temperature, Humidity, BarometricPressure FROM hatdata
#     ORDER BY DateandTime DESC
#     LIMIT 1;
#     """
#     result = myCursor.fetchone(data)
#     with open("webapp/templates/websiteDB.html", "a") as file:
#         file.write("<html> <body> <h1> "+str(result)+" </h1> </body> </html>")


while True:
    temperature, humidity, pressure = GetData()
    ExecuteToDB(temperature, humidity, pressure)
    # ExecuteToWeb()


# thisConn.commit()
# print (temperature, humidity, pressure)
# thisConn.close()
