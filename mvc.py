app = Flask(__name__)
app.config.from_object(__name__)
@app.route('/')
def main_page():
    pass
@app.route('/')
def main_page():
    db = get_db()
    cur = db.execute('select * from entries order by id desc')
    entries = cur.fetchall()
    return render_template('index.html', entries=entries)