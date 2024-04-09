The program is designed to handle various types of mathematical expressions, including:

1. Basic arithmetic expressions: Addition (+), subtraction (-), multiplication (*), and division (/).
2. Exponentiation: Power (^) or double asterisk (**).
3. Parentheses: Nested expressions within parentheses are evaluated first to maintain proper order of operations.
4. Decimal numbers: Numbers with decimal points are supported.
5. Negative numbers: Negative sign (-) preceding a number.
6. Stored values: Users can reference previously stored results using placeholders in the form of "{ID}".

Here are the steps taken to validate a user's input and ensure it conforms to the supported expression types:

1. **Regular Expression Matching**:
   - The `format_input(user_input)` function uses regular expressions to identify and extract valid components of the expression, including operators, numbers, decimal numbers, and placeholders for stored values. This step ensures that only valid characters and expressions are considered for further processing.

2. **Placeholder Substitution**:
   - If the expression contains placeholders for stored values (e.g., "{1}", "{2}"), the program replaces these placeholders with the actual stored values retrieved from the list of stored operations. This ensures that stored values are correctly substituted into the expression before evaluation.

3. **Missing Multiplication Operators**:
   - The program checks for specific cases where multiplication operators may be implicit and inserts them as needed to ensure the expression is well-formed. For example, between a number and an opening parenthesis or between a closing parenthesis and a number.

4. **Handling Negative Numbers**:
   - Special attention is given to handling negative numbers. If a negative sign (-) is detected before a number, the program combines the sign with the following number to form a negative number.

5. **Zero Handling**:
   - There's a specific check to handle cases where a single zero (0) is present in the expression, which may need to be combined with a preceding number to form a valid expression, such as "-0" for negative zero.

6. **Error Handling**:
   - If the input expression is invalid or cannot be processed, appropriate error messages are displayed to the user to indicate the issue. This ensures that users are informed about any errors and can correct their input accordingly.

By following these steps, the program ensures that user input is validated and formatted correctly to be processed as a valid mathematical expression, supporting a wide range of expression types and ensuring accurate calculation results.

Calculating an expression: 
		Finding Brackets:
	•	The function starts by calling find_brackets(expression) to identify all the brackets (both opening and closing) within the expression. This function returns a list containing the indices of all opening and closing brackets in the expression.
		Bracket Processing Loop:
	•	The function then enters a loop to process brackets until none are left. This loop ensures that expressions within brackets are evaluated first.
		Bracket Pair Processing:
	•	Within each iteration of the loop, the function calls get_bracket(brackets, expression) to obtain the start and end indices of a bracket pair.
	•	It extracts the sub-expression enclosed within the bracket pair.
	•	If the sub-expression is not reduced to a single value, it continues to evaluate it until it's reduced to a single value. This ensures nested brackets are processed correctly.
	•	Once the sub-expression is reduced to a single value, it updates the main expression by replacing the sub-expression with its result using the update_expression() function.
		Update Expression:
	•	The update_expression() function is called to replace the portion of the expression enclosed within the brackets with its result. This function takes the original expression, the start and end indices of the sub-expression, and the calculated result as arguments.
	•	The original expression is updated by replacing the sub-expression with its result.
		Loop Continuation:
	•	After updating the expression with the result of the bracket pair, the function checks if there are any remaining brackets in the updated expression.
	•	If there are remaining brackets, it continues the loop to process the next bracket pair.
	•	If no brackets are left, the loop terminates, indicating that all bracket pairs have been processed.
		Expression Evaluation:
	•	Once all bracket pairs are processed and removed from the expression, the function checks if the expression contains only a single value.
	•	If the expression is reduced to a single value, it means the calculation is complete, and the final result is returned.
	•	If the expression still contains operators (such as +, -, *, /, **), it calls the calculate_expression() function to perform the calculation.
		Final Result:
	•	The final result of the expression is returned to the caller, which could be the calculator() function or another part of the program where the expression was originally passed for evaluation.
This process ensures that the mathematical expression is evaluated correctly, following the standard rules of arithmetic operations and respecting the precedence of operators. It handles nested expressions within brackets and ensures that the calculation is performed accurately.
