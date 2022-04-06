from flask import Flask, request, jsonify
from flask_apscheduler import APScheduler
from sql_table import connect_to_db
import sqlite3
from price_getter import insert_btc
app = Flask(__name__)

scheduler = APScheduler()


def schedule():
    insert_btc()


def get_entries(date):
    conn = connect_to_db()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM btc where timestamp='{date}'")
    rows = cur.fetchall()
    return len(list(rows))


def get_prices(date, limit, offset):
    data = []
    conn = connect_to_db()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM btc where timestamp='{date}' LIMIT {limit} OFFSET {offset}")
    rows = cur.fetchall()
    for i in rows:
        data.append({"timestamp": i["timestamp"], "price": int(
            i["price"]), "coin": i["currency"]})
    return data


@app.route('/api/prices', methods=['GET'])
def api_get_users():
    try:
        date, offset, limit = request.args.get("date"), int(
            request.args.get("offset")), int(request.args.get("limit"))
        if not date or not limit:
            return "Please provide query params", 400
        res = {}
        res.update({"url": request.url})
        next_url = f"{request.base_url}?date={request.args.get('date')}" \
            f"&offset={int(request.args.get('offset'))+int(request.args.get('limit'))}" \
            f"&limit={request.args.get('limit')}"
        res.update({"next": next_url})

        count = get_entries(date)
        data = get_prices(date, limit, offset)
        if data == [] or count == 0:
            return "Please check your offset value and other params in the query", 400
        res.update({"count": count})
        res.update({"data": data})
        return jsonify(res)
    except Exception as e:
        return f"Some unexpected error occured {str(e)}. Please contact support", 500



if __name__ == "__main__":
    scheduler.add_job(id='Scheduled Task', func=schedule, trigger="interval", seconds=30)
    scheduler.start()
    app.run(host='localhost',port=5000)
