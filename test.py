import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

db = SQL("sqlite:///finance.db")

test = db.execute("SELECT hash FROM users WHERE id = 1")[0]["hash"]
print(test)