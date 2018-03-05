http://ken.quoit.jp/2011/07/29/%E3%83%A1%E3%83%A2%EF%BC%9Asqlite%E3%81%A7on-update-current_timestamp%E3%82%92%E5%AE%9F%E7%8F%BE%E3%81%99%E3%82%8B/

```sql
CREATE TRIGGER hoge_modified AFTER UPDATE on hoge  
BEGIN  
 UPDATE hoge SET modified = DATETIME("now","localtime") WHERE ID = old.ID;  
END;
```

`hoge`テーブルを更新した後、`modified`列に`DATETIME("now","localtime")`を`SET`する。ただし、`ID`が一致する行のみ。

このトリガーは`hoge_modified`という名前である。

