import tkinter as tk
from time import sleep
from Calculator import solve_expression, format_input, stored_operations, store_operations, access_stored_operations,  expression_stack, step 
import Calculator

Calculator.caller = 'GUI'

"""
Button Layout


AC ( ) / ** 
7 8 9 * ↑ 
4 5 6 - ↓ 
1 2 3 + TAPE 
0 00 . = DEL 
M+ MC M M+ M- 
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
        self.result = None
        self.proof_displayed = False
        
        access_stored_operations(caller='GUI')

        self.buttons = {
        "AC": {"command": "clear", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
        "(": {"command": "open_paren", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
        ")": {"command": "close_paren", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
        "/": {"command": "divide", "state": "normal", "bg": "orange", "key_pressed_bg": "grey"},
        "^": {"command": "power", "state": "normal", "bg": "white", "key_pressed_bg": "grey"},
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
        print('Input Expression: ', user_input_expression)

        # Validate and format the user input expression
        try:
            validated_expression = format_input(user_input_expression, stored_operations)
            # Validate and format the user input expression
            # Create a copy of the validated expression for reference
            working_expression = validated_expression[:]

            # Solve the expression
            result = solve_expression(working_expression)[0]
        except Exception as e:
            # Handle invalid expression
            print(f"Error: {e}")
            result = "Invalid Expression"
        
        print(f"\n\nValidated Expression Processed: {' '.join(validated_expression)} = {result}")

        expression_stack_copy = expression_stack.copy()
        expression_stack_copy.append(f"\nValidated Expression Processed:\n{' '.join(validated_expression)} = {result}")
        self.tape_records.append((validated_expression, result, expression_stack_copy))
                                 
        expression_stack.clear()

        
        return validated_expression, result


    def update_display_after_delay(self, delay_text, delay, text_after_delay):
        self.display.config(text=delay_text)
        self.window.after(delay, lambda: self.display.config(text=text_after_delay))

    def on_button_click(self, operation,caller = 'GUI'):
        
        """
        Handle button clicks.
        
        This method is called when a button is clicked. It updates the display and performs the necessary operations based on the button clicked.
        
        """
    
        if caller == 'GUI':

            print(f"GUI Key Pressed: {operation}")
        else:
            print(f"Physical Key Pressed: {operation}")

    
        if operation == '=':

            if self.buttons_pressed[0] in ['+', '-', '*', '/', '^', '('] and self.result is not None:
                self.buttons_pressed = self.result + self.buttons_pressed
            
            self.working_expression, self.result = self.validate_and_solve_expression(self.buttons_pressed, stored_operations)
            self.display.config(text=self.result)
            
            if self.result != 'Invalid Expression':
                self.memory_add_button.config(state='normal')  

            self.buttons_pressed = ""
        

        elif operation == 'AC':
            self.buttons_pressed = ""
            self.display.config(text='0')

        elif operation == 'DEL':
            self.buttons_pressed = self.buttons_pressed[:-1]
            self.display.config(text=self.buttons_pressed if self.buttons_pressed else '0')
        


        elif operation == 'M+':
            stored_operations.append((' '.join(self.working_expression), self.result))
            store_operations(stored_operations,caller = 'GUI')   
            self.memory_add_button.config(state='disabled')  
            self.memory_remove_button.config(state='normal')
            self.memory_button.config(state='normal')
            self.memory_recall_button.config(state='normal')
            self.memory_clear_button.config(state='normal')

            self.update_display_after_delay(f'Memory Stored {self.result}', 1000, '0')
            self.buttons_pressed = ""

            if self.memory_displayed:
                self.memory_access = len(stored_operations) - 1

                self.display_memory_label.config(text=f"{stored_operations[self.memory_access][0]}\n= {stored_operations[self.memory_access][1]}")

                if len(stored_operations) == 1:
                    self.buttons['\u2191']['button'].config(state = 'disabled')
                    self.buttons['\u2193']['button'].config(state = 'disabled')
                else:
                    self.buttons['\u2191']['button'].config(state = 'normal')
                    self.buttons['\u2193']['button'].config(state = 'disabled')


            print('Stored Operations Updates to include: ',stored_operations[-1])


        elif operation == 'M':
            if self.memory_displayed == False:
                self.memory_access= len(stored_operations) - 1
                print('Memory Access: ',self.memory_access)
                text = f"{stored_operations[self.memory_access][0]}\n= {stored_operations[self.memory_access][1]}" if stored_operations else 'Memory is empty' 
                self.display_memory_label = tk.Label(self.window, text=text,anchor="w",width=40,height=3,padx=5, pady=10,border=3, justify="left",wraplength=370,relief='ridge',)
                self.display_memory_label.grid(row=2, column=0)
                self.memory_displayed = True

                self.buttons['\u2193']['button'].config(state = 'disabled')

                if len(stored_operations) == 0:
                    self.buttons['\u2191']['button'].config(state = 'disabled')
                else:
                    self.buttons['\u2191']['button'].config(state = 'normal')
            
                    
            else:
                self.display_memory_label.destroy()
                self.buttons['\u2191']['button'].config(state = 'disabled')
                self.buttons['\u2193']['button'].config(state = 'disabled')
                self.memory_displayed = False
            
            
            


        elif operation == 'M-':

            if self.memory_displayed:
                text = f'Removed {stored_operations[self.memory_access][1]} from memory'
                stored_operations.pop(self.memory_access)
                store_operations(stored_operations, caller='GUI')
                self.memory_access = len(stored_operations) - 1


                if len(stored_operations) == 1:
                    self.buttons['\u2191']['button'].config(state = 'disabled')
                    self.buttons['\u2193']['button'].config(state = 'disabled')
                else:
                    self.buttons['\u2191']['button'].config(state = 'normal')
                    self.buttons['\u2193']['button'].config(state = 'disabled')
            else:
                print('Stored Operations Updated to exclude: ',stored_operations[-1])

                stored_operations.pop()
                text = f'Removed {stored_operations[-1][1]} from memory'
                store_operations(stored_operations, caller='GUI')

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
                self.display_memory_label.config(text=f'{stored_operations[self.memory_access][0]}\n={stored_operations[self.memory_access][1]}')


        
            
        elif operation == 'MC':

            self.memory_remove_button.config(state='disabled')
            self.memory_add_button.config(state='disabled')
            self.memory_recall_button.config(state='disabled')
            self.memory_remove_button.config(state='disabled')
            self.memory_clear_button.config(state='disabled')
    
            self.buttons['\u2191']['button'].config(state='disabled')
            self.buttons['\u2193']['button'].config(state='disabled')
    
            stored_operations.clear()
            self.memory_access = None
            store_operations(stored_operations, caller='GUI')

        
            self.update_display_after_delay('Memory Cleared', 1000, self.buttons_pressed if self.buttons_pressed else '0')

            if self.memory_displayed:
                self.display_memory_label.config(text='Memory is empty')   

        elif    operation == 'MR':

            access_stored_operations(caller='GUI')

            if self.memory_displayed:
                self.buttons_pressed += (''.join(stored_operations[self.memory_access][1]))

                self.update_display_after_delay(f'Recalled {stored_operations[self.memory_access][1]} from memory', 1000, self.buttons_pressed)
            
            else:
                self.buttons_pressed += (stored_operations[-1][1])
                self.update_display_after_delay(f'Recalled {stored_operations[-1][1]} from memory', 1000, self.buttons_pressed)

        elif operation == 'Insert':
            self.buttons_pressed += (''.join(stored_operations[self.memory_access][1]))
            self.update_display_after_delay(f'Inserted {stored_operations[self.memory_access][1]} from memory', 1000, self.buttons_pressed)


        elif operation == '\u2191':

        
            self.memory_access -=1

            text = f'{stored_operations[self.memory_access][0]}\n= {stored_operations[self.memory_access][1]}'

            self.display_memory_label.config(text=text)   

            print('\u2191 Memory Access: ',self.memory_access)

            if self.memory_access == 0:
                self.buttons['\u2191']['button'].config(state='disabled')
            self.buttons['\u2193']['button'].config(state='normal')


        elif operation == '\u2193': 


            self.memory_access += 1 

            text = f'{stored_operations[self.memory_access][0]}\n= {stored_operations[self.memory_access][1]}'

            self.display_memory_label.config(text=text)

            print('\u2193 Memory Access: ',self.memory_access)

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

                


        else:
            self.buttons_pressed += str(operation)
            self.display.config(text=self.buttons_pressed)
            self.memory_add_button.config(state='disabled')  
    




    def update_tape(self):

        for widget in self.tape_frame.winfo_children():
            widget.destroy()


        if self.proof_displayed == False:
            for index, operation in enumerate(self.tape_records):
                tape_label = tk.Label(self.tape_frame, text=f"Operation {index+1}:\n\n{' '.join(operation[0])}\n = {operation[1]}", anchor="w",width=38, padx=15, border=2, pady=15, justify="left",wraplength=350, relief='ridge')
                tape_label.grid(row=index, column=0, padx=5, pady=5)

        elif self.proof_displayed == 'Simple Workings': 
            for index, operation in enumerate(self.tape_records):
                
                tape_label = tk.Label(self.tape_frame, text=f"Operation {index+1}:\n\n{' '.join(operation[0])}\n = {operation[1]}\n\n {' '.join(str(x) for x in operation[2] if 'Step' in x or 'Expression to Solve' in x or 'Validated Expression Processed' in x)}", anchor="w",width=82, padx=15, border=2, pady=15, justify="left",wraplength=790, relief='ridge')
                tape_label.grid(row=index, column=0, padx=5, pady=5)

        elif self.proof_displayed == 'Detailed Workings':
            for index, operation in enumerate(self.tape_records):
                tape_label = tk.Label(self.tape_frame, text=f"Operation {index+1}:\n\n{' '.join(operation[0])}\n = {operation[1]}\n\n {' '.join(str(x) for x in operation[2])}", anchor="w",width=82, padx=15, border=2, pady=15, justify="left",wraplength=790, relief='ridge')
                tape_label.grid(row=index, column=0, padx=5, pady=5)
    
            
        self.tape.after(100, self.update_tape)  

    def show_proof(self, proof_type):

        if proof_type == self.proof_displayed:
            self.proof_displayed = False
            self.show_proof_simple_button.config(text="Show Simple Workings")
            self.show_proof_button.config(text="Show Detailed Workings")

            self.tape.geometry("400x600+450+0")



        elif proof_type == 'Simple Workings':
            self.proof_displayed = proof_type
            self.show_proof_simple_button.config(text="Hide Simple Workings")
            self.show_proof_button.config(text="Show Detailed Workings")
            self.tape.geometry("800x600+450+0")
        elif proof_type == 'Detailed Workings':
            self.proof_displayed = proof_type
            self.show_proof_button.config(text="Hide Detailed Workings")
            self.show_proof_simple_button.config(text="Show Simple Workings")
            self.tape.geometry("800x600+450+0")
        
            

    def display_tape(self):
        if not hasattr(self, 'tape') or not self.tape.winfo_exists(): 
            self.tape = tk.Toplevel(self.window)
            self.tape.title("Tape")
            self.tape.geometry("400x600+450+0")
            self.tape.resizable(False, False)

            self.tape.bind("<FocusIn>", lambda e: self.tape.focus_set())



            self.clear_button = tk.Button(self.tape, text="Clear", command=lambda: self.tape_records.clear())
            self.clear_button.pack(anchor="e", side="bottom", padx=10, pady=10)

            self.show_proof_button = tk.Button(self.tape, text="Show Detailed Workings", command=lambda: self.show_proof('Detailed Workings'))

            self.show_proof_button.pack(anchor="s", side="bottom", padx=10, pady=10)

            self.show_proof_simple_button = tk.Button(self.tape, text="Show Simple Workings", command=lambda: self.show_proof('Simple Workings'))
            self.show_proof_simple_button.pack(anchor="s", side="bottom", padx=10, pady=10)


            self.canvas = tk.Canvas(self.tape)
            self.scrollbar = tk.Scrollbar(self.tape, orient="vertical", command=self.canvas.yview)

            self.tape_frame = tk.Frame(self.canvas)
            self.tape_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

            self.canvas.create_window((0, 0), window=self.tape_frame, anchor="nw")

            self.canvas.configure(yscrollcommand=self.scrollbar.set)

            self.canvas.pack(side="left", fill="both", expand=True)
            self.scrollbar.pack(side="right", fill="y")

            
            

        self.update_tape() 



        
    def calculator_GUI(self):
        self.frame = tk.Frame(self.window)
        self.frame.grid(row=1, column=0)
        self.frame.focus_set()
        self.frame.bind("<FocusIn>", lambda event: self.frame.focus_set())



    
        self.display = tk.Label(self.window, text="0",anchor="w",padx=5,pady=5, width=40, height=3, border=3, relief='ridge', wraplength= 370, justify="left")
        self.display.grid(row=0, column=0)


        # Create buttons

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

        if len(stored_operations) != 0:
            self.memory_recall_button.config(state='normal')
            self.memory_clear_button.config(state='normal')
            self.memory_remove_button.config(state='normal')



        

        self.frame.bind("<Key>", lambda event : self.on_key_click(event))


    
        
    def on_key_click(self, event):

        key_binds = {
            "<Key-1>": "1", "<Key-2>": "2", "<Key-3>": "3", "<Key-4>": "4", "<Key-5>": "5",
            "<Key-6>": "6", "<Key-7>": "7", "<Key-8>": "8", "<Key-9>": "9", "<Key-0>": "0",
            "<Key-period>": ".",
            "<Key-equal>": "=", "<Key-Return>": "=",
            "<Key-asterisk>": "*", "<Key-minus>": "-", "<Key-plus>": "+", "<Key-slash>": "/", "<Key-asciicircum>": "^",
            "<Key-parenleft>": "(", "<Key-parenright>": ")",
            "<Key-BackSpace>": "DEL", "<Key-c>": "AC",
            "<Key-M>": "M", "<Key-R>": "MR", "<Key-C>": "MC", "<Key-greater>": "M+", "<Key-less>": "M-",
            "<Key-Up>": "\u2191", "<Key-Down>": "\u2193",
            "<Key-T>": "TAPE",
        }

        parsed_keysym = f"<Key-{event.keysym}>"
        if parsed_keysym in key_binds:
            
            self.on_button_click(key_binds[parsed_keysym], caller='Key')
        else:
            print(f'Key Pressed details: Char:{event.char}, Keycode: {event.keycode}, Keysym: {event.keysym}, Keysym_num: {event.keysym_num}\nOperation not found in key binds')
            


    def main(self):
        self.calculator_GUI()
        self.window.mainloop()





if __name__ == "__main__":
    calculator = CalculatorGUI()
    calculator.main()   