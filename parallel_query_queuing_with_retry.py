# Python implementation of a retry function that mimics Oracle’s Parallel Query Statement Queuing. 
# This function waits for available parallel workers before executing the query, rather than immediately 
# downgrading to serial execution. This function checks for parallel worker exhaustion and retries after 
# a delay instead of immediately downgrading to serial execution. You can adjust max_retries and retry_delay 
# to fine-tune behavior. Let me know if you need modifications!

import psycopg2
import time
from psycopg2 import sql

def execute_with_retry(conn, query, max_retries=5, retry_delay=2):
    """
    Executes a PostgreSQL query with retries, mimicking Oracle's Parallel Query Statement Queuing.
    """
    retries = 0
    while retries < max_retries:
        try:
            with conn.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()
        except psycopg2.Error as e:
            if 'parallel worker limit reached' in str(e).lower():
                retries += 1
                time.sleep(retry_delay)  # Wait before retrying
                continue
            else:
                raise  # Raise other database errors
    
    raise Exception("Max retries reached, could not execute query")

# Example usage
if __name__ == "__main__":
    conn = psycopg2.connect("dbname=mydb user=myuser password=mypass host=localhost")
    query = "SELECT * FROM large_table;"
    
    try:
        results = execute_with_retry(conn, query)
        for row in results:
            print(row)
    finally:
        conn.close()
