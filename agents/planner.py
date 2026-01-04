from agents.base_agent import BaseAgent

class PlannerAgent(BaseAgent):
    def run(self, task: str) -> str:
        prompt = f"""
You are an AI planning agent.

Break the following user task into clear, ordered steps.
Do not solve the task.

Task:
{task}

Return only the steps.
"""
        return self.llm.invoke(prompt)
