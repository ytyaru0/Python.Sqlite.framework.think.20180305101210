```python
class MyTable:
    Id = int, PK
    Name = str, UK, NN
    TribeId = int, FK(TribeDb.Tribes.Id)
    Sex1 = int, D(0)
    Sex2 = int, D(MyTable.GetDefaultSex())
    Age1 = int, C(lambda x: 0 <= x and x <= 100)
    Age2 = int, C(lambda x: 0 <= x), C(lambda x: x <= 100)
    Age3 = int, C(is_min=lambda x: 0 <= x, is_max=lambda x: x <= 100)
    Created = datetime
    Some = str, UK, NN, FK()
```

* `./DBMS/SQLite/`配下にDB単位のpackageを作る

たとえば以下。

* `./DBMS/SQLite/`
    * `MyDb/`
        * `MyTables.py`
    * `TribesDb/`
        * `Tribes.py`

上記で以下の2ファイルを作成する。

* `MyDb.sqlite3`
* `TribesDb.sqlite3`

それぞれ以下のテーブルを作成する。
```sh
$ sqlite3 MyDb.sqlite3
sqlite> .tables
MyTables
```
```sh
$ sqlite3 TribesDb.sqlite3
sqlite> .tables
Tribes
```

## Create

https://www.sqlite.org/keyword_index.html

* table
* view
* trigger
* VIRTUAL TABLE
* index
* alert

https://qiita.com/umisama/items/2014f8f09cee447c313f
https://www.sqlite.org/vfs.html

