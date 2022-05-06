class TextEditor():
    """A text editor."""
    
    history = []
    clipboard = []

    def __init__(self, text):
        if text:
            self.text = list(text)

    def __repr__(self):
        return "".join(self.text)
    
    def add_text(self, string):
        text_copy = self.text[:]
        self.history.append(text_copy)
        self.text.append(string)
    
    def delete(self):
        if self.text:
            text_copy = self.text[:]
            self.history.append(text_copy)
            self.text.pop()
    
    def undo(self):
        if self.history:
            self.text = self.history.pop()
    
        
