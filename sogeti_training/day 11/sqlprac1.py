import mysql.connector
def get_connection():
    try:
        connection=mysql.connector.connect(
            host='Ritvik',
            user='root',
            password='!SQLpassword3613',
            database='department'
        )
    except mysql.connector.Error as err:
        print(f'something went wrong {err}')

