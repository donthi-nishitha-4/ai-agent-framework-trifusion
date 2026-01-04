def calculate(expression: str):
    try:
        # Clean up expression
        expression = expression.replace("\n", "").strip()
        # Evaluate safely
        result = eval(expression)
        return result
    except Exception as e:
        return f"Calculation error: {e}"
