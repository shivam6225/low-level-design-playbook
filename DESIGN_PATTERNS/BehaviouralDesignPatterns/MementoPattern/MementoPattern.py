# Undo/Redo -> editor saves snapshot , when we do undo we should we able to move to previous snapshot


#Originator: textEditor
#Memento : snapshot or save point
#Caretaker: Text History class

# TextEditor  --> TextMemento (Dependency)
# TextMemento --<> TextHistory (Aggregation)