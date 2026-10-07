from text_history import History
from text_memento import TextMemento
from text_editor import TextEditor


text_editor = TextEditor()
history = History()
text_editor.write("Good")
text_editor.write(" Morning")
print(text_editor.get_text())
history.save_state(text_editor.save())
text_editor.write(" ,How are you?")
history.save_state(text_editor.save())
print(text_editor.get_text())
history.get_history()
print("----------")
text_editor.restore(history.undo())
print(text_editor.get_text())
text_editor.restore(history.undo())
print(text_editor.get_text())
print("------------")
history.get_redo_stack()
print("------------")
text_editor.restore(history.redo())
print("--Post Redo--")
history.get_redo_stack()
history.get_history()

print(text_editor.get_text())