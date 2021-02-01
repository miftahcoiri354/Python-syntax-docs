# **1. Tutorial Use Flask for Bootstrap**

1. Create a flask python script as `web.py`
2. Download the bootstrap file and extract inside the flask app directory
3. Seperate the static files and move it into `static` folders
4. Seperate the templates files and move it into `templates` folders
5. Then open the `index.html` file and edit the static file directory inside the html code. And add the following syntax before the file directory.
```
"{{ url_for('static', filename=' .... `) }}"
```
6. Then run the python script and evaluate the app on the browser
```
> python web.py
```

# **2. Membuat Program Penjualan dengan Flask Python**

1. Delete all unused page template except the `index.html` 
2. Then open the `index.html' and delete the unused template such as sidebar `menu buttons` and the another `components`
3. Then seperate the index file into 3 parts : `header`, `footer`, 'index' (as main content page). And connect all of 3 different files using syntex belon in the beginning and the end of `index.html` file:
```html
{% include 'header.html'%}
....
{% include 'footer.html'%}
```
4. Delete the unused template by deleting the code in `index.html` from `container-fluid` to the `</div>`.
```html
      <div class="container-fluid">
        
      </div><!-- /.container-fluid -->
```
5. Delete the unused sidebar menu button in `header.html` by removing the code from `Dashboard v1` to `Widget` menu
```html
        <ul class="nav nav-pills nav-sidebar flex-column" data-widget="treeview" role="menu" data-accordion="false">
          <!-- Add icons to the links using the .nav-icon class
               with font-awesome or any other icon font library -->

          <li class="nav-item has-treeview">
```
And also delete the `Charts` menu until the latest `<li>`
```html
          </li>
          
        </ul>
```
And then delete the dropdown list and left only the `Top Navigation`
```html
              </li>
              
            </ul>
```
6. Then change all menu dropdown list with you want:
    - Master Data : Data Barang, Data Supplier, Data Pelanggan
    - Transaksi Pembelian : Form Pembelian, Data Pembelian
    - Transaksi Penjualan : Form Penjualan, Data Penjualan

7. Then create a `html` page for each list menu and connect them all using routing in `web.py`.
  - datapembelian.html
  - datapenjualan.html
  - formpembelian.html
  - formpenjualan.html
  - masterbarang.html
  - masterpelanggan.html
  - mastersupplier.html
  Now, you can run it on the localhost

8. Then modify the active page menu with active status on dropdown list side menu. So, you need add new status variable in `web.py` for each routes by adding `menu` & `submenu`.
```python
@app.route("/masterbarang")
def masterbarang():
    return render_template('masterbarang.html', menu='master', submenu='barang')
``` 
And change the status value in `header.html` page into **Active** status with `{% if menu=='master' %} menu-open {% end if %}`. It will make the menu open when we have clicked on it.
```html
<li class="nav-item has-treeview {% if menu=='master' %} menu-open {% endif %}">
```
But, the submenu still inactive, so we need to add `{% if submenu=='barang' %} active {% endif%}` for each sub menu.
```html
<a href="/masterbarang" class="nav-link {% if submenu=='barang' %} active {% endif%}">
```

# **3. Menampilkan Data Master Barang**

1. Open the `web.py` script and import `MySQL` library and define the `app.config`
```python
from flask_mysqldb import MySQL

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pos'
mysql = MySQL(app)
```
2. Run SQL query language for each route using SQL Language. But, before you run it, make sure you have a created table on MySQL database name `masterbarang`
```python
@app.route("/masterbarang")
def masterbarang():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM masterbarang")
    barang = cur.fetchall()
    cur.close()
    return render_template('masterbarang.html', menu='master', submenu='barang', data=barang)
```
3. 

Connect Python & Database MySQL : [Python MySQL Connector](https://www.youtube.com/watch?v=n_8aA4r6V-o) 