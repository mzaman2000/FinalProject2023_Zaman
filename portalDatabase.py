import mysql.connector
from mysql.connector import Error


class Database():
    def __init__(self,
                 host="localhost",
                 port="3306",
                 database="hospital_portal",
                 user='root',
                 password='Zaman2000'):

        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password)

            if not self.connection.is_connected():
                print("Error: Could not connect to MySQL.")
                self.connection = None
            else:
                self.cursor = self.connection.cursor()

        except Error as e:
            print("Error while connecting to MySQL", e)
            self.connection = None

    def addPatient(self, patient_name, patient_id, age, admission_date, discharge_date):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "INSERT INTO patients (patient_name, patient_id, age, admission_date, discharge_date) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(
                query, (patient_name, patient_id, age, admission_date, discharge_date))
            self.connection.commit()
            return

    def getAllPatients(self):

        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM patients"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records

    def scheduleAppointment(self, patient_id, doctor_id, appointment_date, appointment_time):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(
                query, (patient_id, doctor_id, appointment_date, appointment_time))
        self.conn.commit()
        print("Appointment scheduled successfully.")
        return

    def viewAppointments(self):
        if self.connection and self.connection.is_connected():
            self.cursor.execute("SELECT * FROM appointments")
            appointments = self.cursor.fetchall()
            return appointments

    def dischargePatient(self, patient_id):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "DELETE FROM patients WHERE patient_id = %s"
            self.cursor.execute(query, (patient_id,))
            self.connection.commit()
            return
