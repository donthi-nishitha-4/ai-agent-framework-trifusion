from fastapi import FastAPI
from pydantic import BaseModel

from llm.llm_client import get_llm
from agents.planner import PlannerAgent
from agents.reasoner import ReasonerAgent
from agents.executor import ExecutorAgent
from memory.short_term import ShortTermMemory

app = FastAPI(title="AI Agent Framework – Ollama LLaMA-3")

llm = get_llm()
memory = ShortTermMemory()

planner = PlannerAgent(llm, memory)
reasoner = ReasonerAgent(llm, memory)
executor = ExecutorAgent()

class AgentRequest(BaseModel):
    query: str

@app.post("/agent")
def run_agent(req: AgentRequest):
    plan = planner.run(req.query)
    action = reasoner.run(plan)
    result = executor.execute(action)

    memory.add({
        "query": req.query,
        "plan": plan,
        "action": action,
        "result": result
    })

    return {
        "plan": plan,
        "action": action,
        "result": result
    }
