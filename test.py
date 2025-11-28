import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

db = SQL("sqlite:///finance.db")

print(db.execute("SELECT cash FROM users WHERE username = ?", 123))
print(db.execute("SELECT username FROM users"))

db.execute("UPDATE users SET cash = cash + ? WHERE username = ?", 500, 123)
