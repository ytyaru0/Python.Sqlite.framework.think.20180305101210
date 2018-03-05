try:
    import MyTable
except NameError as e:
    print(e)
    import importlib
    importlib.import_module('Constraints')
    # 現在 locals() にある module に Constraints.py モジュールを加える。
    # （MyTableにConstraintsを加える。`from Constraints import PK,UK,FK,NN,D,C`する）

    # トレースバックで例外発生モジュールを補足
    import sys, traceback
    exc_type, exc_value, exc_traceback = sys.exc_info()
    last_tb = None
    for tb in traceback.extract_tb(exc_traceback):
        print(tb)
        last_tb = tb
    #print(last_tb)
    #print(type(last_tb))
    #print(dir(last_tb))
    print(last_tb.filename)
    print(last_tb.line)
    print(last_tb.lineno)
    print(last_tb.name)
    import pathlib
    module_path = pathlib.Path(last_tb.filename)
    module_name = module_path.name.replace(module_path.suffix, '')
    print(module_name)

    # モジュール インスタンスに Constraints を挿入しようと思ったが、できない。PK未定義エラーのため。
    # ソースコードを文字列で作成すればいいか？ `from Constraints import PK,UK,FK,NN,D,C`を加えて。
    # exec(source_code)すればいい？
    #import importlib
    #importlib.import_module(module_name)
    print(e)
    #print('未定義', e)
    #print(type(e))
    #print(dir(e))
    #print(e.args)
    #print(type(e.with_traceback()))
    #print(e.with_traceback())
    #print(type(e.with_traceback))
    #print(dir(e.with_traceback))

    # #!python3などの行が先頭にあるが処理省略！
    source_code = 'from Constraints import PK,UK,FK,NN,D,C' + '\n'
    with pathlib.Path(last_tb.filename).open() as f:
        source_code += f.read()

    exec(source_code)
    assert(module_name in locals())
    cls = locals()[module_name]
    print(dir(cls))
    print(cls.Id)
    # name 'PK' is not defined

    #print(locals())
    #print(locals()['__loader__'])
    #print(dir(locals()['__loader__']))
    #print(locals()['__loader__'].get_filename())
