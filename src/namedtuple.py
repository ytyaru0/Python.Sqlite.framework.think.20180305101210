# namedtupleは、classとproperty(getter,setter)を作ってくれる。
from collections import namedtuple
db_name = 'MyDb'
table_name = 'MyTable'
column_names = ['Id','Age','Name','TribeId']
nt_MyDb = namedtuple(table_name, column_names, module=db_name)
print(nt_MyDb)
print(type(nt_MyDb))
for column in column_names:
    print(getattr(nt_MyDb, column))

rec1 = nt_MyDb(0, 0, 'A', 0)
rec2 = nt_MyDb(Id=0, Age=0, Name='A', TribeId=0)
rec3 = nt_MyDb(*[0, 0, 'A', 0])
rec4 = nt_MyDb(**{'Id':0, 'Age':0, 'Name':'A', 'TribeId':0})
print(rec1)
print(rec2)
print(rec3)
print(rec4)
