#from copy import deepcopy

class TextEditor():
    """A text editor."""
    
    text = [] #list of characters
    history = [] #a stack with latest history stored last
    clipboard = []

    cursor = 0

    def __init__(self, text):
        """When initializing text editor, given text is stored as individual characters in a list.
            This allows for adding cursor position later."""
        if text:
            self.text = list(text)

    def __repr__(self):
        return "".join(self.text)
    
    def add(self, text):
        """Add new text to the end of text"""
        text_copy = self.text[:] #or use deepcopy
        self.history.append(text_copy)
        new_text = list(text)
        self.text.extend(new_text)
    
    def insert(self, text):
        """Add new text given a cursor position.
            Set new cursor position."""
        text_copy = self.text[:] #or use deepcopy
        self.history.append(text_copy)
        new_text = list(text)
        
    
    def delete(self):
        """If text exists, remove the last character"""
        if self.text:
            text_copy = self.text[:] #or use deepcopy
            self.history.append(text_copy)
            self.text.pop() #delete last character
    
    def undo(self):
        if self.history:
            self.text = self.history.pop()

    def copy(self):


    def paste(self):
    
        
