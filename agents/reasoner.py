from agents.base_agent import BaseAgent

class ReasonerAgent(BaseAgent):
    def run(self, plan: str) -> str:
        prompt = f"""
You are a reasoning agent.

Given the plan below, decide the next action.
If a calculation is required, respond exactly in this format:

calculate <expression>

Otherwise, respond with a short answer.

Plan:
{plan}
"""
        return self.llm.invoke(prompt)
