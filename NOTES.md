
CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL, hash TEXT NOT NULL, cash NUMERIC NOT NULL DEFAULT 10000.00)
;
CREATE TABLE sqlite_sequence(name,seq);


CREATE UNIQUE INDEX username ON users (username);
CREATE TABLE orders (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, type TEXT, symbol TEXT, shares INTEGER, total_price REAL,time TEXT);

db.execute(
    """INSERT INTO orders (username, type, symbol, shares, total_price, time)
    VALUES (?, ?, ?, ?, ?, ?)""", session["user_id"], "buy", request.form.get("stock") ,request.form.get("shares"), total_price, datetime('now')
)