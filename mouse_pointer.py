from Xlib import display

def get_mouse_position():
    data = display.Display().screen().root.query_pointer()._data
    return data["root_x"], data["root_y"]

x, y = get_mouse_position()
print("Mouse position - X:", x, "Y:", y)

