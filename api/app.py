import psycopg2
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/dog_names')
def doggos():
    url = "https://data.world/anchorage/a9a7-y93v/file/dog-names-from-march-2022-1.csv"
    df = pd.read_csv(url)
    conn = psycopg2.connect(database = 'anchorage_dog_names', user = 'Sonja')
    #df.to_sql('dog_names', conn, index = False)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dog_names')
    

#C:\Users\Sonja\practice\code\flask-project-lab\flask-project-lab\migrations\create_tables.sql