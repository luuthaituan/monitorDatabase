from sshtunnel import SSHTunnelForwarder
import mysql.connector

# SSH connection details
ssh_host = '192.168.56.34'
ssh_username = 'thaituan'
ssh_password = 'tuan89'

# MySQL connection details
mysql_host = '127.0.0.1'
mysql_port = 3306
mysql_database = 'test'
mysql_username = 'root'
mysql_password = 'tuan89'

try:
    # Create the SSH tunnel
    with SSHTunnelForwarder(
        (ssh_host, 22),
        ssh_username=ssh_username,
        ssh_password=ssh_password,
        remote_bind_address=(mysql_host, mysql_port)
    ) as tunnel:
        # Connect to MySQL through the SSH tunnel
        db = mysql.connector.connect(
            host='127.0.0.1',
            port=tunnel.local_bind_port,
            user=mysql_username,
            password=mysql_password,
            database=mysql_database
        )
        print("Connected to MySQL database successfully!")
except Exception as e:
    print(f"Failed to connect to MySQL database: {e}")