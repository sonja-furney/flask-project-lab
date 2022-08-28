import sqlite3 
from flask import Flask, jsonify
import psycopg2
import os

from dotenv import load_dotenv

load_dotenv()

DB_NAME= os.getenv("DATABASE")
user= os.getenv("user")