from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pos'
mysql = MySQL(app)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/masterbarang")
def masterbarang():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM masterbarang")
    barang = cur.fetchall()
    cur.close()
    return render_template('masterbarang.html', menu='master', submenu='barang', data=barang)

@app.route("/mastersupplier")
def mastersupplier():
    return render_template('mastersupplier.html', menu='master', submenu='supplier')

@app.route("/masterpelanggan")
def masterpelanggan():
    return render_template('masterpelanggan.html', menu='master', submenu='pelanggan')

@app.route("/formpembelian")
def formpembelian():
    return render_template('formpembelian.html', menu='pembelian', submenu='formpembelian')

@app.route("/datapembelian")
def datapembelian():
    return render_template('datapembelian.html', menu='pembelian', submenu='datapembelian')

@app.route("/formpenjualan")
def formpenjualan():
    return render_template('formpenjualan.html', menu='penjualan', submenu='formpenjualan')

@app.route("/datapenjualan")
def datapenjualan():
    return render_template('datapenjualan.html', menu='penjualan', submenu='datapenjualan')

if __name__=="__main__":
    app.run(debug=True)