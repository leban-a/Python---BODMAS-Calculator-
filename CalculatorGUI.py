import tkinter as tk
from time import sleep
from Calculator import solve_expression, format_input, stored_operations, store_operations

"""Button Layout
["AC", "(", ")", "/", "^", 
 "7", "8", "9", "*", "{", 
 "4", "5", "6", "-", "}", 
 "1", "2", "3", "+", "M+", 
 "0", "00", ".", "=", "DEL"]
 """

class CalculatorGUI:

    
    def __init__(self):


        self.window = tk.Tk()
        self.window.title("Calculator")

        self.buttons_pressed = ""
        self.memory_access = None
        self.memory_displayed = False
        self.tape_records = []
        self.tape_displayed = False

        self.buttons = {
        "AC": {"command": "clear", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
        "(": {"command": "open_paren", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
        ")": {"command": "close_paren", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
        "/": {"command": "divide", "state": "normal", "bg": "orange", "key_pressed_bg": "grey"},
        "**": {"command": "power", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
        "7": {"command": "seven", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
        "8": {"command": "eight", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
        "9": {"command": "nine", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
        "*": {"command": "multiply", "state": "normal", "bg": "orange", "key_pressed_bg": "grey"},
        "\u2191": {"command": "open_brace", "state": "disabled", "bg": "white", "key_pressed_bg": "grey"},
        "4": {"command": "four", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
        "5": {"command": "five", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
        "6": {"command": "six", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
        "-": {"command": "subtract", "state": "normal", "bg": "orange", "key_pressed_bg": "grey"},
        "\u2193": {"command": "close_brace", "state": "disabled", "bg": "white", "key_pressed_bg": "grey"},
        "1": {"command": "one", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
        "2": {"command": "two", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
        "3": {"command": "three", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
        "+": {"command": "add", "state": "normal", "bg": "orange", "key_pressed_bg": "grey"},
        "TAPE": {"command": 'display_tape', "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
        "0": {"command": "zero", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
        "00": {"command": "double_zero", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
        ".": {"command": "decimal", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
        "=": {"command": "equals", "state": "normal", "bg": "orange", "key_pressed_bg": "grey"},
        "DEL": {"command": "delete", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
        }    




    def validate_and_solve_expression(self, user_input_expression, stored_operations):


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
        
        print(f"Expression: {validated_expression} = {result}")

        self.tape_records.append((validated_expression, result))
        
        return validated_expression, result


    def update_display_after_delay(self, delay_text, delay, text_after_delay):
        self.display.config(text=delay_text)
        self.window.after(delay, lambda: self.display.config(text=text_after_delay))

    def on_button_click(self, operation):

        print(f"Button {operation} clicked!")


        if operation == '=':

            if self.buttons_pressed[0] in ['+', '-', '*', '/', '**', '('] and self.result:
                self.buttons_pressed = self.result + self.buttons_pressed
            
            self.working_expression, self.result = self.validate_and_solve_expression(self.buttons_pressed, stored_operations)
            self.display.config(text=self.result)
            
            if self.result != 'Invalid Expression':
                self.memory_add_button.config(state='normal')  # Update the button's state

            self.buttons_pressed = ""
        

        elif operation == 'AC':
            self.buttons_pressed = ""
            self.display.config(text='0')

        elif operation == 'DEL':
            self.buttons_pressed = self.buttons_pressed[:-1]
            self.display.config(text=self.buttons_pressed if self.buttons_pressed else '0')
        


        elif operation == 'M+':
            stored_operations.append((self.working_expression, self.result))
            self.memory_add_button.config(state='disabled')  # Update the button's state
            self.memory_remove_button.config(state='normal')
            self.memory_button.config(state='normal')
            self.memory_recall_button.config(state='normal')
            self.memory_clear_button.config(state='normal')

            self.update_display_after_delay(f'Memory Stored {self.result}', 1000, '0')
            self.buttons_pressed = ""

            if self.memory_displayed:
                self.memory_access = len(stored_operations) - 1

                self.display_memory_label.config(text=f"{' '.join(stored_operations[-1][0])}\n= {stored_operations[-1][1]}")

                if len(stored_operations) == 1:
                    self.buttons['\u2191']['button'].config(state = 'disabled')
                    self.buttons['\u2193']['button'].config(state = 'disabled')
                else:
                    self.buttons['\u2191']['button'].config(state = 'normal')
                    self.buttons['\u2193']['button'].config(state = 'disabled')


            print(stored_operations)


        elif operation == 'M':
            if self.memory_displayed == False:
                self.memory_access= len(stored_operations) - 1
                text = f"{' '.join(stored_operations[self.memory_access][0])}\n = {stored_operations[self.memory_access][1]}" if stored_operations else 'Memory is empty' 
                self.display_memory_label = tk.Label(self.window, text=text,anchor="w",width=40,height=2,padx=5, pady=10,border=3, relief='ridge',)
                self.display_memory_label.grid(row=2, column=0)
                self.memory_displayed = True
            else:
                self.display_memory_label.destroy()
                self.memory_displayed = False
            
            if len(stored_operations) == 1:
                self.buttons['\u2191']['button'].config(state = 'disabled')
                self.buttons['\u2193']['button'].config(state = 'disabled')
            else:
                self.buttons['\u2191']['button'].config(state = 'normal')


        elif operation == 'M-':

            if self.memory_displayed:
                text = f'Removed {stored_operations[self.memory_access][1]} from memory'
                stored_operations.pop(self.memory_access)
                self.memory_access = len(stored_operations) - 1


                if len(stored_operations) <= 1:
                    self.buttons['\u2191']['button'].config(state = 'disabled')
                    self.buttons['\u2193']['button'].config(state = 'disabled')
                else:
                    self.buttons['\u2191']['button'].config(state = 'normal')
                    self.buttons['\u2193']['button'].config(state = 'disabled')
            else:
                text = f'Removed {stored_operations[-1][1]} from memory'
                stored_operations.pop()

            self.update_display_after_delay(text, 1000, self.buttons_pressed if self.buttons_pressed else '0')


            
            if len(stored_operations)  == 0:
                self.memory_add_button.config(state='disabled')
                self.memory_recall_button.config(state='disabled')
                self.memory_remove_button.config(state='disabled')
                self.memory_clear_button.config(state='disabled')
                if self.memory_displayed:
                    self.display_memory_label.config(text='Memory is empty')
                    self.buttons['\u2191']['button'].config(state='disabled')
                    self.buttons['\u2193']['button'].config(state='disabled')
            elif self.memory_displayed:
                self.display_memory_label.config(text=f'{" ".join(stored_operations[self.memory_access][0])}\n= {stored_operations[self.memory_access][1]}')


        
            
            print(stored_operations)
        elif operation == 'MC':

            self.memory_remove_button.config(state='disabled')
            self.memory_add_button.config(state='disabled')
            self.memory_recall_button.config(state='disabled')
            self.memory_remove_button.config(state='disabled')
            self.memory_clear_button.config(state='disabled')
            stored_operations.clear
            self.update_display_after_delay('Memory Cleared', 1000, self.buttons_pressed if self.buttons_pressed else '0')
            self.display_memory_label.config(text='Memory is empty')   

        elif    operation == 'MR':

            if self.memory_displayed:
                self.buttons_pressed += (stored_operations[self.memory_access][1])

                self.update_display_after_delay(f'Recalled {stored_operations[self.memory_access][1]} from memory', 1000, self.buttons_pressed)
            
            else:
                self.buttons_pressed += (stored_operations[-1][1])
                self.update_display_after_delay(f'Recalled {stored_operations[-1][1]} from memory', 1000, self.buttons_pressed)

        elif operation == 'Insert':
            self.buttons_pressed += (stored_operations[self.memory_access][1])
            self.update_display_after_delay(f'Inserted {stored_operations[self.memory_access][1]} from memory', 1000, self.buttons_pressed)


        elif operation == '\u2191':
        
            self.memory_access -= 1
            text = f'{' '.join(stored_operations[self.memory_access][0])}\n = {stored_operations[self.memory_access][1]}'
            self.display_memory_label.config(text=text)   
            print('up',self.memory_access)
            if self.memory_access == 0:
                self.buttons['\u2191']['button'].config(state='disabled')
                
            self.buttons['\u2193']['button'].config(state='normal')


        elif operation == '\u2193': 
    
            self.memory_access += 1
            text = f'{' '.join(stored_operations[self.memory_access][0])}\n = {stored_operations[self.memory_access][1]}'
            self.display_memory_label.config(text=text)
            print('down',self.memory_access)
            if self.memory_access == len(stored_operations) - 1:
                self.buttons['\u2193']['button'].config(state='disabled')
            self.buttons['\u2191']['button'].config(state='normal')
    
        elif operation == 'TAPE':

            if self.tape_displayed:
                self.tape.destroy()
                self.tape_displayed = False
            else:

                self.tape_displayed = True
                self.display_tape()
                self.window.focus_set()


        else:
            self.buttons_pressed += str(operation)
            self.display.config(text=self.buttons_pressed)
            self.memory_add_button.config(state='disabled')  



    def update_tape(self):
        for widget in self.tape_frame.winfo_children():
            widget.destroy()

        for index, operation in enumerate(self.tape_records):
            tape_label = tk.Label(self.tape_frame, text=f"{' '.join(operation[0])}\n= {operation[1]}", anchor="w", width=30, height=2, padx=5, border=0, pady=15)
            tape_label.grid(row=index, column=0)

        self.tape.after(1000, self.update_tape)  


    def display_tape(self):
        if not hasattr(self, 'tape') or not self.tape.winfo_exists():
            self.tape = tk.Toplevel(self.window)
            self.tape.title("Tape")
            self.tape.geometry("300x400+450+0")
            self.tape.resizable(False, False)

            self.canvas = tk.Canvas(self.tape)
            self.scrollbar = tk.Scrollbar(self.tape, orient="vertical", command=self.canvas.yview)

            self.tape_frame = tk.Frame(self.canvas)
            self.tape_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

            self.canvas.create_window((0, 0), window=self.tape_frame, anchor="nw")

            self.canvas.configure(yscrollcommand=self.scrollbar.set)

            self.canvas.pack(side="left", fill="both", expand=True)
            self.scrollbar.pack(side="right", fill="y")

            self.clear_button = tk.Button(self.tape, text="Clear", command=lambda: self.tape_records.clear())
            self.canvas.create_window(290, 390, window=self.clear_button, anchor="se")


        self.update_tape()  

        
    def calculator_GUI(self):
        # Create a frame
        self.frame = tk.Frame(self.window)
        self.frame.grid(row=1, column=0)


    
        # Create a label for the display
        self.display = tk.Label(self.window, text="0",anchor="w",padx=5,pady=5, width=40, height=3, border=3, relief='ridge',)
        self.display.grid(row=0, column=0)



        for index, i in enumerate(self.buttons.keys()):
            button = tk.Button(self.frame, text=i, state=self.buttons[i]['state'],width=5, bg='blue', command=lambda i=i: self.on_button_click(i))    
            button.grid(row=index//5, column=index%5)
            self.buttons[i]['button'] = button  


        self.memory_recall_button= tk.Button(self.frame, text="MR", state="disabled",width=5, bg='white', command=lambda: self.on_button_click("MR"))
        self.memory_recall_button.grid(row=6, column=0)
        
        self.memory_clear_button= tk.Button(self.frame, text="MC", state="disabled",width=5, bg='white', command=lambda: self.on_button_click("MC"))
        self.memory_clear_button.grid(row=6, column=1)

        self.memory_button = tk.Button(self.frame, text="M", state="normal",width=5, bg='white', command=lambda: self.on_button_click("M"))
        self.memory_button.grid(row=6, column=2)

        self.memory_add_button= tk.Button(self.frame, text="M+", state="disabled",width=5, bg='white', command=lambda: self.on_button_click("M+"))
        self.memory_add_button.grid(row=6, column=3)


        self.memory_remove_button= tk.Button(self.frame, text="M-", state="disabled",width=5, bg='white', command=lambda: self.on_button_click("M-"))
        self.memory_remove_button.grid(row=6, column=4)

        
    

    def main(self):
        self.calculator_GUI()
        self.window.mainloop()





if __name__ == "__main__":
    calculator = CalculatorGUI()
    calculator.main()