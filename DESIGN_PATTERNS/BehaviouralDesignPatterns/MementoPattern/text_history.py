from text_memento import TextMemento
from typing import List

class History:
    def __init__(self):
        self.__history:List[TextMemento] = []
        self.__redo_stack: List[TextMemento] = []

    def save_state(self,tm:TextMemento):
        self.__history.append(tm)

    def get_history(self) :
        for i in range(len(self.__history)):
            print(f"{i} = {self.__history[i].get_saved_text()}")

    def get_redo_stack(self) :
        for i in range(len(self.__redo_stack)):
            print(f"{i} = {self.__redo_stack[i].get_saved_text()}")

    def undo(self):
        if len(self.__history) > 0:
            #First move to Redo
            self.__redo_stack.append(self.__history[-1])
            #The pop from history
            self.__history.pop()
            if len(self.__history) > 0:
                return TextMemento(self.__history[-1].get_saved_text())
            else:
                return TextMemento("")
        else:
            return TextMemento("")

    def redo(self):
        if len(self.__redo_stack) <= 0:
            return TextMemento("")
        else:
            self.__history.append(self.__redo_stack[-1])
            self.__redo_stack.pop()
            if len(self.__history) > 0:
                return TextMemento(self.__history[-1].get_saved_text())
            else:
                return TextMemento("")

