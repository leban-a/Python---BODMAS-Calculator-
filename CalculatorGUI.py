import tkinter as tk
from Calculator import solve_expression, format_input, stored_operations

def validate_and_solve_expression(user_input_expression, stored_operations):


    try:
        # Validate and format the user input expression
        validated_expression = format_input(user_input_expression, stored_operations)
        # Create a copy of the validated expression for reference
        working_expression = validated_expression[:]

        # Solve the expression
        result = solve_expression(working_expression)[0]
    except:
        # Handle invalid expression
        result = "Invalid Expression"
    
    return result

# Create a variable to store the buttons pressed
buttons_pressed = ""



def on_button_click(operation):
    global buttons_pressed

    if operation == '=':
        result = validate_and_solve_expression(buttons_pressed, stored_operations)
        display.config(text=result)
        buttons_pressed = ""
    elif operation == 'AC':
        buttons_pressed = ""
    elif operation == 'DEL':
        buttons_pressed = buttons_pressed[:-1]
    else:
        buttons_pressed += str(operation)
        display.config(text=buttons_pressed)
    print(f"Button {operation} clicked!")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create a frame
frame = tk.Frame(window)
frame.grid(row=1, column=0)

# Create a label for the display
display = tk.Label(window, text="0",anchor="w",padx=5, width=40, height=3, border=3, relief='ridge',)
display.grid(row=0, column=0)

# Create buttons for operations
buttons = {
    "AC": {"command": "clear", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
    "(": {"command": "open_paren", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
    ")": {"command": "close_paren", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
    "/": {"command": "divide", "state": "normal", "bg": "orange", "key_pressed_bg": "grey"},
    "^": {"command": "power", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
    "7": {"command": "seven", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
    "8": {"command": "eight", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
    "9": {"command": "nine", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
    "*": {"command": "multiply", "state": "normal", "bg": "orange", "key_pressed_bg": "grey"},
    "{": {"command": "open_brace", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
    "4": {"command": "four", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
    "5": {"command": "five", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
    "6": {"command": "six", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
    "-": {"command": "subtract", "state": "normal", "bg": "orange", "key_pressed_bg": "grey"},
    "}": {"command": "close_brace", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
    "1": {"command": "one", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
    "2": {"command": "two", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
    "3": {"command": "three", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
    "+": {"command": "add", "state": "normal", "bg": "orange", "key_pressed_bg": "grey"},
    "M+": {"command": "memory_add", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
    "0": {"command": "zero", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
    "00": {"command": "double_zero", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
    ".": {"command": "decimal", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
    "=": {"command": "equals", "state": "normal", "bg": "orange", "key_pressed_bg": "grey"},
    "DEL": {"command": "delete", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
}
"""
["AC", "(", ")", "/", "^", 
 "7", "8", "9", "*", "{", 
 "4", "5", "6", "-", "}", 
 "1", "2", "3", "+", "M+", 
 "0", "00", ".", "=", "DEL"]
 """

for index, i in enumerate(buttons.keys()):
    button = tk.Button(frame, text=i, state=buttons[i]['state'],width=5, bg='blue', command=lambda i=i: on_button_click(i))    
    button.grid(row=index//5, column=index%5)

window.mainloop()