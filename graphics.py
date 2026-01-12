import tkinter as tk

##########################################################################
# Module Exceptions
class GraphicsError(Exception):
    """Generic error class for graphics module exceptions."""
    pass

OBJ_ALREADY_DRAWN = "Object currently drawn"
UNSUPPORTED_METHOD = "Object doesn't support operation"
BAD_OPTION = "Illegal option value"


############################################################################
# Graphics classes start here
class CanvasFrame(tk.Frame):
    """A CanvasFrame is a frame for displaying graphics."""

    def __init__(self, parent, width=200, height=200):
        super().__init__(parent)
        self.parent = parent
        self.canvas = tk.Canvas(parent, width=width, height=height)
        self.canvas.pack()
        parent.resizable(False, False)
        self.items = []
        self.mouseX = None
        self.mouseY = None
        self.canvas.bind("<Button-1>", self._onClick)
        self.height = height
        self.width = width
        self._mouseCallback = None
        self.closed = False
        parent.lift()

    def __checkOpen(self):
        if self.closed:
            raise GraphicsError("window is closed")

    def setBackground(self, color):
        self.__checkOpen()
        self.canvas.config(bg=color)

    def close(self):
        if not self.closed:
            self.closed = True
            self.parent.destroy()

    def isClosed(self):
        return self.closed

    def flush(self):
        self.__checkOpen()
        self.update_idletasks()

    def bindMouse(self, func):
        """Bind a callback function for mouse clicks."""
        self._mouseCallback = func

    def _onClick(self, event):
        self.mouseX = event.x
        self.mouseY = event.y
        if self._mouseCallback:
            self._mouseCallback(event)

    def drawRect(self, x1, y1, x2, y2, fill="black"):
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline="black")
