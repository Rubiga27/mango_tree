def is_mango_tree(rows, columns, tree_number):
    if tree_number <= columns or tree_number % columns == 1:
        return True
    else:
        return False
        
rows = int(input("Rows: "))
columns = int(input("Columns: "))
tree_number = int(input("Tree count: "))
if is_mango_tree(rows, columns, tree_number):
    print("True")
else:
    print("False")