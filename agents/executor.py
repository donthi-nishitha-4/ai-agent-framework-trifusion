import re
from tools.calculator import calculate

class ExecutorAgent:
    def execute(self, action: str):
        action = action.strip().lower()

        # Look for "calculate <expression>" anywhere
        match = re.search(r'calculate\s+([0-9\.\+\-\*\/\s\(\)]+)', action)
        if match:
            expression = match.group(1).strip()
            print(f"DEBUG: Evaluating expression: '{expression}'")  # <--- ADD THIS
            return calculate(expression)

        return action
