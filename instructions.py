from texteditor import TextEditor

editor = TextEditor('Happy')
print(editor)
editor.delete()
print(editor)
editor.undo()
editor.add(' Birthday!')
print(editor)
editor.set_cursor(0)
print(editor)
editor.insert('Wish you a very ')
print(editor)
editor.copy(0,4)
print(editor)
editor.reset_cursor()
print(editor)
editor.delete_given_position()
print(editor)
editor.paste()
print(editor)