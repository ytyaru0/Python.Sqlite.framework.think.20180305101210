# https://docs.python.org/ja/3.6/library/ast.html
import ast
source = ''
#source += "col_name = 'COLMUN_NAME'\n" # '=' SyntaxError: invalid syntax
#source = 'a + 5'
#source = '0 < 5'
source += 'col_name < 5'
#source = 'lambda x: 0 < x' # check ( 0 < {col_name} )
#source = 'lambda x: 0 < x and x < 100' # check ( 0 < {col_name} and {col_name} < 100)  
root_node = ast.parse(source, mode='eval')

# 抽象構文木を再帰処理
def recursion(node):
    print(type(node))
    print(*ast.iter_fields(node))
    for n in ast.iter_child_nodes(node):
        recursion(n)

recursion(root_node)

