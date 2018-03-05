# SQLite VFS

SQLiteでファイルシステム(FS)操作ができる？　調べてみたができなかった。C++で実装せねばならない？

* https://qiita.com/umisama/items/2014f8f09cee447c313f
* https://www.sqlite.org/vfs.html
* https://docs.python.jp/3/library/sqlite3.html#sqlite3.connect
* https://www.sqlite.org/uri.html

```python
>>> import sqlite3
>>> con = sqlite3.connect('file:/tmp/test.db?vfs=unix')
>>> cur = con_vfs.cursor()
>>> res = cur.execute('select * from sqlite_master')
>>> res.rowcount
-1
```

もしかして、Python標準のsqlite3では使えない？

APSWはSQLiteの様々な機能が使えるラッパらしい。

* https://rogerbinns.github.io/apsw/vfs.html
* https://qiita.com/mima_ita/items/711f4324da14cbd7741c

以下を見ると、FSを操作できるわけではなさそう。「DBファイルにINSERTするときのデータを、バイナリレベルで加工できる」。暗号化などで使えるが、べつにSQLiteの外側でやってもいい気がする。

* https://qiita.com/mima_ita/items/711f4324da14cbd7741c#virtual-file-system-vfs%E3%81%8C%E4%BD%BF%E7%94%A8%E5%8F%AF%E8%83%BD%E3%81%A7%E3%81%82%E3%82%8B


## 結論

VFSは「DBファイルにINSERTするときのデータを、バイナリレベルで加工できる」機能。

ただ、フック(hook)できるので、自前で実装すれば何でもできそう。`insert`したときにMastodonのtootをするとか。

