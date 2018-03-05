class MyTable:
    Id = int, PK, AUTO
    Name = str, UK, NN, C(lambda x: 0 < len(x) and len(x) < 80)
    TribeId = int, FK(TribeDb.Tribes.Id)
    Sex = int, D(0), C(lambda x: x in [0,1])
    Age = int, D(0), C(lambda x: x in [0,1])
