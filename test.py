import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

db = SQL("sqlite:///finance.db")

test0 = db.execute("SELECT SUM(shares) AS total_shares FROM orders WHERE symbol = 'AAPL' AND user_id = 1")

test1 = db.execute("SELECT SUM(shares) AS total_shares FROM orders WHERE symbol = 'AAPL' AND user_id = 1")[0]['total_shares']
test2 = db.execute("SELECT shares AS total_shares FROM orders WHERE symbol = 'AAPL' AND user_id = 1")

print(test0)
print(test1)
print(test2)

