
"""
Test File for Calculator Module

This test file provides functions to test expressions against expected results.

Functions:
- test_expressions(user_input_expression_list, expected_results_list=None): Function to test a list of expressions against expected results.

Dependencies:
- format_input: A function from the Calculator module to validate and format user input expressions.
- solve_expression: A function from the Calculator module to solve expressions.

Optional Dependency:
- tabulate: A third-party library used for tabular output. If tabulate is available, the test results will be displayed in a table format; otherwise, the results will be printed in a simple format.

"""


#Import dependencies
from Calculator import format_input, solve_expression, stored_operations

# Attempt to import tabulate
try:
    from tabulate import tabulate
    TABULATE_AVAILABLE = True
except ImportError:
    TABULATE_AVAILABLE = False

def print_table(data, headers):
    """
    Print tabular data using tabulate with text wrapping.

    Args:
    - data (list): List of rows to be printed.
    - headers (list): List of column headers.

    Returns:
    - None
    """
    print("\n\n")
    if TABULATE_AVAILABLE:
        print(tabulate(data, headers=headers, tablefmt="grid", stralign="wrap"))
    else:
        for row in data:
            print("  ".join(row))
    print("\n\n")


def test_expressions(user_input_expression_list):
    """
    Test a list of expressions against expected results.

    Args:
    - user_input_expression_list (list): A list of tuples, where each tuple contains the expression and its expected result.
    - expected_results_list (list, optional): A list of expected results corresponding to each input expression. Defaults to None.

    Returns:
    - None
    """
    # Table headers
    headers = ["Input Expression", "Validated Expression", "Result", "Expected Result", "Test"]

    # Table data
    table_data = []

    # Iterate through the list of user input expressions and their corresponding indices
    for user_input_expression, expected_result in user_input_expression_list:
        
        
        # Validate and format the user input expression
        validated_expression = format_input(user_input_expression, stored_operations)
        # Create a copy of the validated expression for reference
        working_expression = validated_expression[:]
        try:
            # Solve the expression
            result = solve_expression(working_expression)[0]
        except:
            # Handle invalid expression
            result = "Invalid Expression"

        # Check if expected results are provided
        if expected_result:
            # Compare the result with the expected result
            test_result = 'Passed' if result == expected_result else 'Failed'
            # Append data to table
            table_data.append([user_input_expression, ' '.join(validated_expression), str(result), str(expected_result), test_result])
        else:
            # Append data to table
            table_data.append([user_input_expression, ' '.join(validated_expression), str(result), "", ""])

    # Print table or fallback to original printing
    print_table(table_data, headers)


# Stored operations
stored_operations = [
    (['-', '1', '**', '4', '/', '23'], '-5.0'),                                 # Placeholder test 1
    (['-', '5', '+', '3', '*', '(', '7', '/', '2', ')', '**', '2'], '-5.0'),    # Placeholder test 2
    (['15', '/', '3'], '1.0'),                                                  # Placeholder test 3
    (['3', '*', '(', '4', '+', '5', ')'], '11.0'),                              # Placeholder test 4
    (['10', '-', '2', '*', '3', '+', '5', '**', '2'], '29.0'),                  # Placeholder test 5
    (['-', '1', '**', '4', '/', '23'], '-5.0'),                                 # Placeholder test 6 

]


user_input_expression_list = [

    
    
    ("(500 / 121 / 165 * 0.5 - 10000 - -54232423) * (600 - -6) - -6", "32858788351.58827948910593539"),  # Complex expression with multiple operations
    ("(600 - -650) - -2343 / 32 * (73 - -5 ** 5 / 7 ** 5) * (400)", "2144683.054679597786636520497"),    # Complex expression with nested operations and exponentiation
    ("70054 / 454 * (54545) + (5 ** 30)", "931322574615486932134.7577093"),                              # Complex expression with large exponentiation
    ("(2 + 3) * 4", "20"),                                                                               # Simple expression with addition and multiplication
    ("1.5 * (3 + 4)", "10.5"),                                                                           # Expression with decimal multiplication
    ("10 / 2 - 3", "2"),                                                                                 # Simple expression with division and subtraction
    ("5 + -3", "2"),                                                                                     # Simple expression with addition and unary negation (Corrected to "2")
    ("2 ** 3", "8"),                                                                                     # Exponential expression
    ("2 ** (3 + 1)", "16"),                                                                              # Exponential expression with addition
    ("2 * (3 + 4)", "14"),                                                                               # Expression with multiplication and addition
    ("2 * 3 + 4", "10"),                                                                                 # Expression with multiplication and addition
    ("2.5 * 2", "5.0"),                                                                                  # Decimal multiplication
    ("5 / 0", "Invalid Expression"),                                                                     # Division by zero
    ("5 / (3 - 3)", "Invalid Expression"),                                                               # Division resulting in infinity
    ("5 + 3", "8"),                                                                                      # Simple expression with addition
    ("5 - -3", "8"),                                                                                     # Expression with subtraction and double negative
    ("-(3 + 2) * 4", "-20"),                                                                             # Expression with unary negation
    ("2(3 * 4)", "24"),                                                                                  # Expression with implicit multiplication
    ("5 * (3 + 4)", "35"),                                                                               # Expression with multiplication and addition
    ("(2 * 3) ** 2 + 4", "40"),                                                                          # Expression with exponentiation("-({1} ** 4 / 23) - -5 * (400 / {3})", "-5.0"),                  
    ("(-5 + 3 * ({2} / {1}) ** 2) * (2 + 3)", "-10"),                                                    # Placeholder test 1
    ("({5} / {3}) ** 2 - ({4} - 2 * {2})", "820.0"),                                                     # Placeholder test 2
    ("{3} * ({4} + {5}) - ({6} / 2) ** 2", "33.75"),                                                     # Placeholder test 3
    ("({1} - 2 * {3}) + {5} ** 2", "834.00"),                                                            # Placeholder test 4
    ("a + b + c", 'Invalid Expression'),                                                                 # Alphabaet expression
    ("", 'Invalid Expression'),                                                                          # Empty expression
    ("5 + 6 - 7 * 8 / 9 * (10 + 5**2)","-206.7777777777777777777777778"),                                # Complex expression with all BODMAS operations in reverse order



]

test_expressions(user_input_expression_list)
