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
    
    def set_cursor(self, position):
        """Change cursor position (int)"""
        if position:
            self.cursor = position

    def reset_cursor(self):
        """Set cursor position to the end of text"""
        self.cursor = len(self.text)
    
    def add(self, text):
        """Add new text to the end of text"""
        text_copy = self.text[:] #or use deepcopy
        self.history.append(text_copy)
        new_text = list(text)
        self.text.extend(new_text)
        #set cursor to the end of text
        self.cursor = len(self.text)
    
    def insert(self, text, cursor=cursor):
        """Add new text given a cursor position.
            Set new cursor position."""
        text_copy = self.text[:] #or use deepcopy
        self.history.append(text_copy)
        new_text = list(text)
        #slice list based on cursor position
        before = self.text[:cursor]
        after = self.text[cursor:]
        self.text = before + new_text + after
        #set new cursor at end of new text
        self.cursor = len(before)+len(new_text)
    
    def delete(self):
        """If text exists, remove the last character"""
        if self.text:
            text_copy = self.text[:] #or use deepcopy
            self.history.append(text_copy)
            self.text.pop() #delete last character
            #set cursor to end of text
            self.cursor = len(self.text)
    
    def delete_given_position(self):
        """Delete one character before cursor."""
        if self.text:
            text_copy = self.text[:] #or use deepcopy
            self.history.append(text_copy)
            #slice at cursor, exclude cursor
            before = self.text[:self.cursor-1]
            after = self.text[self.cursor:]
            self.text = before + after
            #set cursor to end of text
            self.cursor = len(self.text)
    
    def undo(self):
        """Revert to before last change"""
        if self.history:
            self.text = self.history.pop()

    def copy(self, position1, position2):
        """Given two positions, copy everything in between to clipboard.
            Does not change text"""
        copy_text = self.text[position1:position2]
        self.clipboard.append(copy_text)

    def paste(self):
        """Add text in clipboard to cursor position"""
        text_copy = self.text[:] #or use deepcopy
        self.history.append(text_copy)
        new_text = self.clipboard.pop()
        #slice list based on cursor position
        before = self.text[:self.cursor]
        after = self.text[self.cursor:]
        self.text = before + new_text + after
        #set new cursor at end of new text
        self.cursor = len(before)+len(new_text)

    def cut(self, position1, position2):
        """Given two positions, copy everything in between to clipboard.
            Remove copied text"""
        before = self.text[:position1]
        cut_text = self.text[position1:position2]
        after = self.text[position2:]
        self.text = before + after
        self.clipboard.append(cut_text)
        #set cursor to cut position
        self.cursor = position1

    def forward_delete(self):
        """Remove one character after cursor position"""
        if self.text:
            text_copy = self.text[:] #or use deepcopy
            self.history.append(text_copy)
            #slice at cursor, exclude cursor
            before = self.text[:self.cursor]
            after = self.text[self.cursor+1:]
            self.text = before + after

    def redo(self):
        pass

 
