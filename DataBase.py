import mysql.connector
import logging

# Logger setup
logging.basicConfig(filename='school_system.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class Database:
    def __init__(self):
        """Establish database connection"""
        self.conn = mysql.connector.connect(host='localhost', user='root', password='Gh14_az03_zl25', database='school_db')
        self.cursor = self.conn.cursor()
        logging.info("Database connection established")
    
    def execute_query(self, query, values=None):
        """Execute insert, delete, or update queries"""
        self.cursor.execute(query, values) if values else self.cursor.execute(query)
        self.conn.commit()
        
    def fetch_results(self, query, values=None):
        """Fetch results from the database and ensure it returns an iterable"""
        self.cursor.execute(query, values) if values else self.cursor.execute(query)
        results = self.cursor.fetchall()  
        return results if results else [] 

    def close(self):
        """Close database connection"""
        self.conn.close()
        logging.info("Database connection closed")

