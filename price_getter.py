from pycoingecko import CoinGeckoAPI
from sql_table import connect_to_db
from datetime import datetime
from dotenv import load_dotenv
from email_sender import send
import os
load_dotenv()
cg = CoinGeckoAPI()


def insert_btc():
    conn = connect_to_db()
    cur = conn.cursor()
    res = cg.get_price(ids='bitcoin', vs_currencies='usd')
    if int(res["bitcoin"]["usd"]) < int(os.getenv("min")) or int(res["bitcoin"]["usd"]) > int(os.getenv("max")):
        send(int(res["bitcoin"]["usd"]))
    cur.execute("INSERT INTO btc (price,timestamp,currency) VALUES (?, ?, ?)",
                (res["bitcoin"]["usd"], datetime.utcnow().strftime("%d-%m-%Y"), "btc"))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    insert_btc()
