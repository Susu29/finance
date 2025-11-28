import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

db = SQL("sqlite:///finance.db")

user_transactions = db.execute("SELECT * FROM orders WHERE user_id = 1")
for transaction in user_transactions:
    print(transaction["type"])
    
