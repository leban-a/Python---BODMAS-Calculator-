#Calculator Program

#This is a simple calculator program implemented in Python. It allows users to perform basic arithmetic operations and store previous calculations for later use.

#Features


#Arithmetic operations: Addition, subtraction, multiplication, division, and exponentiation.
#Implicit multiplication: Automatically handles multiplication between certain elements of an expression without the need for explicit multiplication symbols.
#Store previous calculations: Allows users to store the results of calculations for future reference.
#Retrieve stored calculations: Provides functionality to access and display previously stored calculations.
#Validate and format user input: Ensures that user input is valid and properly formatted for accurate expression evaluation.

#Usage

#Launch the application by running calculator.py.
#Choose an option from the main menu.
#Follow the prompts to input your expression or select other options.
#View the result and choose whether to store it or perform another operation.
#Viewthe stored calculations by selecting the "History" option from the menu or when prompted.
#Use stored values by using value {ID}
#Exit the program by typing exit


import re
from decimal import Decimal
import sys 


# List to store previous calculations
stored_operations = []

# Function to launch the application
def main():
    """
    Function to launch the application, displaying an application launch message
    and providing instructions for navigating the main menu or exiting the program.
    """
    # Display application launch message
    print("\n\nApplication Launching\n\n")
    print("Type 'menu' to return to the main menu at any time. Type 'exit' to end the program.\n\n")
    # Call the main menu function
    menu()

# Function to display the main menu and handle user input
def menu():
    """
    Function to display the main menu, provide instructions, and handle user input
    for selecting different options. It prompts the user to choose an option from
    the menu, gets user input, and executes the corresponding function based on 
    the input received.
    """
    # Display main menu
    print("\n\nMain Menu\n\n")    
    # Instructions for selecting an option
    instructions = "Please select an option from the menu below:\n\n1: Calculator\n"
    # Get user choice and execute corresponding function
    menu_option = get_input('menu_options', instructions)
    menu_option(stored_operations)

# Function to operate the calculator
def calculator(stored_operations):
    """
    Function to operate the calculator. It allows users to input an expression
    to solve, validates and formats the input, solves the expression, and displays
    the result. Users can also choose to view previously saved calculations, and
    the option to store the current calculation result.

    Args:
    - stored_operations (list): A list of previously stored calculations.

    Returns:
    - None
    """

    
    # Check if there are previously stored calculations
    if stored_operations:
        # Ask user if they want to view previous calculations
        instruction = "You have previously saved calculations. Would you like to view them? (Y/N)"
        if get_input('access_stored_operations', instruction):
            access_stored_operations()

    # Get expression from user
    user_input_expression = get_input('get_expression', "Enter an expression to solve:")
    # Validate and format user input
    validated_expression = format_input(user_input_expression, stored_operations)
    working_expression = validated_expression[:]

    # Output the result of the calculation
    output_result(validated_expression, user_input_expression, working_expression, stored_operations)

    # Reset the calculator
    reset()

    
# Function to output the result of the calculation
def output_result(validated_expression, user_input_expression, working_expression, stored_operations):
    """
    Function to output the result of the calculation.

    Args:
    - validated_expression (list): The validated expression to be solved.
    - user_input_expression (str): The original user input expression.
    - original_expression (list): The original expression before validation and formatting.

    Returns:
    - None
    """
    try: 
        # Solve the expression
        result = solve_expression(working_expression)[0]
    except:
        # Handle invalid expression
        result = "Invalid Expression"

    if result == "Invalid Expression":
        # Display error message for invalid expression
        print(f"\n\nInput:\n{user_input_expression}\nOutput:\n{' '.join(validated_expression)}\n\n{result}")
    else:
        # Display validated expression and result
        print(f"\nUser Input: \n{user_input_expression}\n\nValidated Expression: \n{' '.join(validated_expression)} = {result}\n")
        # Store the calculation
    stored_operations = store_operations(stored_operations, result, validated_expression)


# Function to access previously stored calculations
def access_stored_operations():
    """
    Function to access previously stored calculations. It displays stored
    calculations along with their IDs, allowing users to refer to them in
    subsequent calculations by their ID enclosed in curly brackets.

    Args:
    - None

    Returns:
    - None
    """
    if len(stored_operations) > 0:
        # Display stored calculations
        print("These are your stored calculations:\n\n")
        print("IDs\n")
        for index, pack in enumerate(stored_operations):
            calculation = pack[0]
            result = pack[1]
            print(f"{index+1}: {' '.join(calculation)} = {result}\n")
        print('To use the result of any of the calculations listed, input the respective ID encased in curly brackets example: \'{1}\'.\nEnsuring that the an operator is placed before or after where needed.')
    else: 
        # Inform user of no stored calculations
        print("You have no stored calculations")


# Function to store calculation results
def store_operations(stored_operations, result, calculation):
    """
    Function to store calculation results based on user input. It prompts the
    user whether they want to store the result. If the user chooses to store
    the result, it appends the calculation and its result to the stored_operations
    list. It also notifies the user about the successful storage of the result
    and how to access and use these values in subsequent calculations.

    Args:
    - stored_operations (list): List containing previously stored calculations.
    - result (str): Result of the current calculation.
    - calculation (list): List representing the expression of the current calculation.

    Returns:
    - stored_operations (list): Updated list of stored calculations.
    """
    instruction = f"Would you like to store the result: {result}"
    # Ask user if they want to store the result
    store_operation = get_input('store', instruction) 
     
    if store_operation:
        # Store the result
        stored_operations.append((calculation, result))
        print("The results of your calculation are now stored. \nTo access and use these values type \'History\' when prompted.")
    else: 
        # Inform user that result was not stored
        print("The result of your calculation was not stored.")
    return stored_operations


# Function to get user input
def get_input(type, instructions=None):
    """
    Function to get user input based on the specified type of input.

    Args:
    - type (str): Type of input being requested.
    - instructions (str or list): Instructions to be displayed for the user.

    Returns:
    - User input or corresponding function based on the input type.
    """
    input_valid = False

    while not input_valid: 
        print("")
        # Print instructions if provided
        if instructions == None:
            pass
        elif isinstance(instructions, str):
            print(instructions) 
        else:
            for instruction in instructions:
                print(instruction)

        user_input = input("> ")

        # Check if user wants to exit
        if user_input.lower() == "exit":
            input_valid = True 
            exit_program()

        # Menu options
        if type == 'menu_options':
            if user_input in ["1", 'calculator']:
                input_valid = True
                return calculator
            elif user_input.lower() in ['2', 'stored operations']:
                input_valid = True
                return access_stored_operations

        # Return to main menu
        elif user_input.lower() == 'menu':
            input_valid = True 
            menu()

        # Access stored operations
        elif user_input.lower() == 'history':
            access_stored_operations()
            continue

        # Reset calculator
        elif type == 'reset':
            if user_input == '':
                input_valid = True 
                calculator(stored_operations)
            else:
                input_valid = False

        # Get expression from user
        elif type == 'get_expression':
            input_valid = True
            return user_input

        # Store result of calculation
        elif type == 'store':
            if user_input.lower() in ['yes', 'y']:
                input_valid = True
                return True    
            elif user_input.lower() in ['no', 'n']:
                input_valid = True
                return False 
            else: 
                input_valid = False

        # Access stored operations
        elif type == 'access_stored_operations':
            if user_input.lower() in ['y', 'yes']:
                input_valid = True
                return True
            elif user_input.lower() in ['n', 'no']:
                input_valid = True
                return False
            else: 
                input_valid = False

        # Notify if input is not recognized
        if input_valid == False:
            print(f"\n\nYour response: {user_input} was not recognised\n\n")


# Function to reset the calculator
def reset():
    """
    Function to reset the calculator after performing an operation.

    This function prompts the user to either perform another operation or exit the program.

    Returns:
    - None
    """
    instruction = "\nTo perform another operation hit enter or type 'exit' to end the program."
    get_input('reset', instruction)


# Function to solve an expression
def solve_expression(expression):
    """
    Function to solve a mathematical expression.

    Args:
    - expression (list): The list representing the expression to be solved.

    Returns:
    - result: The result of the expression after evaluation.
    """
    # Find all brackets in the expression
    brackets = find_brackets(expression)

    # Continue looping until the expression is reduced to a single value
    while len(expression) != 1:
        # Continue processing brackets until none are left
        while brackets:
            # Get the start and end indices of a bracket pair
            start, end = get_bracket(brackets, expression)
            # Extract the sub-expression within the brackets
            sub_expression = expression[start + 1:end] 

            # Continue evaluating the sub-expression until it's reduced to a single value
            while len(sub_expression) != 1:
                # If the main expression is already reduced to a single value, use the sub-expression itself
                sub_expression = sub_expression if len(expression) == 1 else calculate_expression(sub_expression)
            
            # Update the expression by replacing the sub-expression with its result
            expression = update_expression(expression=expression, sub_expression=sub_expression, start=start, end=end)
            # Find brackets again in the updated expression
            brackets = find_brackets(expression)

        # Calculate the expression if it still contains operators
        expression = expression if len(expression) == 1 else calculate_expression(expression)

    # Return the final result
    result = expression
    return result



# Function to perform a calculation within an expression
def calculate_expression(expression):
    """
    Perform a calculation within an expression.

    Args:
    - expression (list): List representing the expression to be calculated.

    Returns:
    - Updated expression after the operation.
    """
    # Perform the operation and get the result along with the index of the operator
    result, index = perform_operation(expression)
    # Replace the operator with the result in the expression
    expression[index] = str(result)
    # Update the expression after the operation
    expression = update_expression(expression, index)
    # Return the updated expression
    return expression



# Function to update an expression after performing a calculation
def update_expression(expression, index=None, sub_expression=None, start=None, end=None):
    """
    Update an expression after performing a calculation.

    Args:
    - expression (list): List representing the expression to be updated.
    - index (int): Index of the operator to be replaced with the result.
    - sub_expression (list): List representing the sub-expression with the result.
    - start (int): Start index of the sub-expression.
    - end (int): End index of the sub-expression.

    Returns:
    - Updated expression after the operation.
    """
    # If sub_expression is provided, replace the portion of the expression with the result
    if sub_expression: 
        return expression[:start] + [sub_expression[0]] + expression[end + 1:]
    # If index is provided, replace the operator with the result in the expression
    else: 
        return expression[:index - 1] + [expression[index]] + expression[index + 2:]


# Function to perform a specific operation in an expression
def perform_operation(expression):
    """
    Perform a specific operation in an expression.

    Args:
    - expression (list): List representing the expression.

    Returns:
    - Tuple containing the result of the operation and the index of the operator.
    """
    # Extract operators from the expression
    operators = re.findall(r'\(|\)|\*\*|[*/+\-]', ''.join(expression))
    
    # Iterate through each symbol in the list of symbols
    for i in ['**', '/', '*', '+', '-'] :
        # Check if the symbol exists in the operators list
        if i not in operators:
            continue

        # Iterate through the expression to find the index of the symbol
        for index, n in enumerate(expression):
            # If the symbol is found
            if i == n:
                # Define the operation based on the symbol
                if expression[index] == '**': 
                    operation = lambda a,b: a**b    
                elif expression[index] == '/': 

                    operation = lambda a,b: a/b
                elif expression[index] == '*': 
                    operation = lambda a,b: a*b
                elif expression[index] == '+': 
                    operation = lambda a,b: a+b
                elif expression[index] == '-': 
                    operation = lambda a,b: a-b
        
                # Get the operands (numbers) before and after the operator
                a = expression[index - 1]
                b = expression[index + 1]

                # Perform the operation on the operands and return the result along with the index of the operator
                return operation(Decimal(a), Decimal(b)), index

# Function to get start and end indices of a bracket pair
def get_bracket(brackets, expression):
    """
    Get the start and end indices of a bracket pair in an expression.

    Args:
    - brackets (list): List of indices representing brackets in the expression.
    - expression (list): List representing the expression.

    Returns:
    - Tuple containing the start and end indices of the bracket pair.
    """
    # Iterate through the list of bracket indices
    for i in brackets:
        # Check if the character at the current index is an opening bracket '('
        if expression[i] == '(':
            # Set the start index to the current index
            start = i
        # Check if the character at the current index is a closing bracket ')'
        elif expression[i] == ')':
            # Set the end index to the current index
            end = i
            # Break the loop once the closing bracket is found
            break
    # Return the start and end indices of the bracket pair
    return start, end



# Function to find all brackets in an expression
def find_brackets(expression):
    """
    Find all brackets in an expression and return their indices.

    Args:
    - expression (list): List representing the expression.

    Returns:
    - List containing the indices of all opening and closing brackets in the expression.
    """
    # Create a list comprehension to iterate over each character in the expression
    # and generate a list of indices for opening and closing brackets
    brackets = [index for index, char in enumerate(expression) if char in ['(', ')']]
    # Return the list of bracket indices
    return brackets


# Function to format user input into a valid expression
def format_input(user_input,stored_operations):
    """
    Format user input into a valid expression.

    Args:
    - user_input (str): User input representing the expression.

    Returns:
    - List containing components of the formatted expression.
    """
    # Use regular expression to find all valid components of the expression,
    # including operators, numbers, decimal numbers, and placeholders for stored values
    formatted_input = re.findall(r'\(|\)|\*\*|[*/+\-]|{\d+}|\d+\.\d+|\d+|^\-\d+|^\-\d+\.\d+|\-\-', user_input)
    # Check and modify the expression for validity
    return check_expression(formatted_input,stored_operations)


# Function to check and modify expressions for validity
def check_expression(expression,stored_operations):
    """
    Check and modify expressions for validity.

    Args:
    - expression (list): List representing the expression.

    Returns:
    - List containing the modified expression.
    """
    # Start iterating over the expression
    index = -1
    
    while index != len(expression):
        index += 1
        

        if index == 0 and expression[index] == '-' and expression[index+1] == "(":
            expression.insert(0,'0')
        try: 
            if expression[index] == '-' and expression[index+1] == '-' and expression[index+2] == '(':
                expression[index] = '+'
                expression.pop(index+1)
                index -= 1 
        except:
            pass
    
        try: 
            # Check if the current component is a placeholder for a stored value
            if expression[index].startswith('{') and expression[index].endswith('}'):
                # Retrieve the stored value from the list of stored operations
                _ , value = stored_operations[int(expression[index].strip("{}"))-1]
                
                
                # Check if the previous component is a negative sign
                if expression[index-1][0] == '-':
                    # Change the sign of the stored value to positive
                    value = abs(value)
                # Replace the placeholder with the actual value
                expression[index] = value
            
                if expression[index-1].isdecimal() and index != 0 or expression[index-1]==')':
                    expression.insert(index-1, '*')
                    index -=1


                elif expression[index+1].isdecimal() or expression[index+1]== '(':
                    expression.insert(index+1, '*')
                    index -=1

        except:
            pass

        try: 
            # Check for specific cases where a multiplication operator is missing
            if (expression[index] == ')' and expression[index + 1] == '(') : 
                # Insert a multiplication operator between adjacent parentheses
                expression.insert(index + 1, '*')
                index -=1

            elif (expression[index].isdecimal() and expression[index + 1] == '(') or \
                 (expression[index + 1].isdecimal() and expression[index] == ')'):
                # Insert a multiplication operator between a number and a following parenthesis or vice versa
                expression.insert(index + 1, '*')
                index -=1
        except:
            pass

        if index - 1 <= -1: 
            continue
        # Handle cases where a negative sign should be part of a number
        elif expression[index-1] == '-' and (index == 1 or expression[index-2] in ['(','**', '/', '*', '+', '-']):
            expression[index] =  expression[index-1] + expression[index] 
            expression.pop(index-1)
            index -=1
        if len(expression) ==  2 and expression[index] == 0 and expression[index].isdecimal():
            expression[index]=expression[index-1]+expression[index]
            expression.pop(index-1)
            index -=1

        

        
    return expression


# Function to exit the program
def exit_program():
    """
    Exit the program.

    This function displays an exit message, sets a flag to indicate program termination,
    and terminates the program.
    """
    # Display exit message
    print("\n\nYou've chosen to exit the program.")
    print("\nProgram will now end.\n\n")

    # Terminate the program
    sys.exit(0)



# Main function
if __name__ == '__main__': 
    # Call the main function to start the program
    main()

